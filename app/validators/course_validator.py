def validate_course_payload(body):
    if not body:
        return "Request body is missing"

    required_fields = ["title", "duration", "price"]
    for field in required_fields:
        if field not in body:
            return f"{field} is required"

    return None