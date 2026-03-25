def validate_person_payload(body):
    if not body:
        return "Request body is missing"

    required_fields = ["first_name", "last_name", "email"]
    for field in required_fields:
        if field not in body:
            return f"{field} is required"

    return None