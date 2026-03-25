from flask import Blueprint, jsonify, request
from app.services.booking_service import (
    create_booking,
    get_all_bookings,
    get_booking_by_id,
    delete_booking,
)
from app.validators.booking_validator import validate_booking_payload

booking_bp = Blueprint("bookings", __name__, url_prefix="/bookings")


@booking_bp.post("/")
def create_booking_route():
    body = request.get_json()

    error = validate_booking_payload(body)
    if error:
        return jsonify({"message": error}), 400

    booking, service_error = create_booking(
        body["person_id"],
        body["course_id"],
    )

    if service_error == "person_not_found":
        return jsonify({"message": "Person not found"}), 404

    if service_error == "course_not_found":
        return jsonify({"message": "Course not found"}), 404

    return jsonify(booking), 201


@booking_bp.get("/")
def get_all_bookings_route():
    return jsonify(get_all_bookings()), 200


@booking_bp.get("/<uuid:booking_id>")
def get_booking_route(booking_id):
    booking = get_booking_by_id(booking_id)
    if booking is None:
        return jsonify({"message": "Booking not found"}), 404

    return jsonify(booking), 200


@booking_bp.delete("/<uuid:booking_id>")
def delete_booking_route(booking_id):
    deleted_booking = delete_booking(booking_id)

    if deleted_booking is None:
        return jsonify({"message": "Booking not found"}), 404

    return jsonify({
        "message": f"Booking with {booking_id} deleted",
        "booking": deleted_booking
    }), 200
