import uuid
from app.data.store import persons


def create_person(first_name, last_name, email):
    new_person = {
        "id": str(uuid.uuid4()),
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
    }
    persons.append(new_person)
    return new_person


def get_all_persons():
    return persons


def get_person_by_id(person_id):
    for person in persons:
        if person["id"] == str(person_id):
            return person
    return None


def update_person(person_id, first_name, last_name, email):
    person = get_person_by_id(person_id)
    if person is None:
        return None

    person["first_name"] = first_name
    person["last_name"] = last_name
    person["email"] = email
    return person


def delete_person(person_id):
    person = get_person_by_id(person_id)
    if person is None:
        return None

    persons.remove(person)
    return person