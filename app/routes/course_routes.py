from flask import Blueprint, jsonify, request
from app.services.course_service import (
    create_course,
    get_all_courses,
    get_course_by_id,
    update_course,
    delete_course,
)
from app.validators.course_validator import validate_course_payload

course_bp = Blueprint("courses", __name__, url_prefix="/courses")


@course_bp.post("/")
def create_course_route():
    body = request.get_json()

    error = validate_course_payload(body)
    if error:
        return jsonify({"message": error}), 400

    course = create_course(
        body["title"],
        body["duration"],
        body["price"],
    )
    return jsonify(course), 201


@course_bp.get("/")
def get_all_courses_route():
    return jsonify(get_all_courses()), 200


@course_bp.get("/<uuid:course_id>")
def get_course_route(course_id):
    course = get_course_by_id(course_id)
    if course is None:
        return jsonify({"message": "Course not found"}), 404

    return jsonify(course), 200


@course_bp.put("/<uuid:course_id>")
def update_course_route(course_id):
    body = request.get_json()

    error = validate_course_payload(body)
    if error:
        return jsonify({"message": error}), 400

    updated_course = update_course(
        course_id,
        body["title"],
        body["duration"],
        body["price"],
    )

    if updated_course is None:
        return jsonify({"message": "Course not found"}), 404

    return jsonify(updated_course), 200


@course_bp.delete("/<uuid:course_id>")
def delete_course_route(course_id):
    deleted_course = delete_course(course_id)

    if deleted_course is None:
        return jsonify({"message": "Course not found"}), 404

    return jsonify({
        "message": f"Course with {course_id} deleted",
        "course": deleted_course
    }), 200