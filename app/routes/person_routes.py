from flask import Blueprint, jsonify, request
from app.services.person_service import (
    create_person,
    get_all_persons,
    get_person_by_id,
    update_person,
    delete_person,
)
from app.validators.person_validator import validate_person_payload

person_bp = Blueprint("persons", __name__, url_prefix="/persons")


@person_bp.post("/")
def create_person_route():
    body = request.get_json()

    error = validate_person_payload(body)
    if error:
        return jsonify({"message": error}), 400

    person = create_person(
        body["first_name"],
        body["last_name"],
        body["email"],
    )
    return jsonify(person), 201


@person_bp.get("/")
def get_all_persons_route():
    return jsonify(get_all_persons()), 200


@person_bp.get("/<uuid:person_id>")
def get_person_route(person_id):
    person = get_person_by_id(person_id)
    if person is None:
        return jsonify({"message": "Person not found"}), 404

    return jsonify(person), 200


@person_bp.put("/<uuid:person_id>")
def update_person_route(person_id):
    body = request.get_json()

    error = validate_person_payload(body)
    if error:
        return jsonify({"message": error}), 400

    updated_person = update_person(
        person_id,
        body["first_name"],
        body["last_name"],
        body["email"],
    )

    if updated_person is None:
        return jsonify({"message": "Person not found"}), 404

    return jsonify(updated_person), 200


@person_bp.delete("/<uuid:person_id>")
def delete_person_route(person_id):
    deleted_person = delete_person(person_id)

    if deleted_person is None:
        return jsonify({"message": "Person not found"}), 404

    return jsonify({
        "message": f"Person with {person_id} deleted",
        "person": deleted_person
    }), 200