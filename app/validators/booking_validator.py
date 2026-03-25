def validate_booking_payload(body):
    if not body:
        return "Request body is missing"

    required_fields = ["person_id", "course_id"]
    for field in required_fields:
        if field not in body:
            return f"{field} is required"

    return None