import uuid
from app.data.store import bookings
from app.services.person_service import get_person_by_id
from app.services.course_service import get_course_by_id


def create_booking(person_id, course_id, status="confirmed"):
    person = get_person_by_id(person_id)
    if person is None:
        return None, "person_not_found"

    course = get_course_by_id(course_id)
    if course is None:
        return None, "course_not_found"

    new_booking = {
        "id": str(uuid.uuid4()),
        "person_id": str(person_id),
        "course_id": str(course_id),
        "status": status,
    }
    bookings.append(new_booking)
    return new_booking, None


def get_all_bookings():
    return bookings


def get_booking_by_id(booking_id):
    for booking in bookings:
        if booking["id"] == str(booking_id):
            return booking
    return None


def delete_booking(booking_id):
    booking = get_booking_by_id(booking_id)
    if booking is None:
        return None

    bookings.remove(booking)
    return booking