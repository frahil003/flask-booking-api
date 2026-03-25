import uuid
from app.data.store import courses


def create_course(title, duration, price):
    new_course = {
        "id": str(uuid.uuid4()),
        "title": title,
        "duration": duration,
        "price": price,
    }
    courses.append(new_course)
    return new_course


def get_all_courses():
    return courses


def get_course_by_id(course_id):
    for course in courses:
        if course["id"] == str(course_id):
            return course
    return None


def update_course(course_id, title, duration, price):
    course = get_course_by_id(course_id)
    if course is None:
        return None

    course["title"] = title
    course["duration"] = duration
    course["price"] = price
    return course


def delete_course(course_id):
    course = get_course_by_id(course_id)
    if course is None:
        return None

    courses.remove(course)
    return course