# Flask Booking API

A modular REST API built with Flask that manages **Persons**, **Courses**, and **Bookings**. The project demonstrates clean architecture (routes, services, validators), UUID-based identifiers, and full CRUD operations.

---

## 🚀 Features

- **Persons API** (CRUD)
- **Courses API** (CRUD)
- **Bookings API** (Create, Read, Delete)
- UUID-based resource identification
- Separation of concerns (Routes / Services / Validators)
- In-memory data storage (easy to swap with a DB later)

---

## 🧱 Architecture

```text
app/
├── routes/        # HTTP layer (Flask Blueprints)
├── services/      # Business logic
├── validators/    # Request validation
├── data/          # In-memory storage
└── __init__.py    # App factory
```

---

## 🛠 Tech Stack

- Python 3
- Flask
- UUID (built-in)

---

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/flask-booking-api.git
cd flask-booking-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python run.py
```

API base URL:

```
http://localhost:5000
```

---

# 📡 API Overview

## 👤 Persons

### Create

```
POST /persons/
```

```json
{
  "first_name": "Susi",
  "last_name": "Sonnenschein",
  "email": "susi@example.com"
}
```

### Get all

```
GET /persons/
```

### Get one

```
GET /persons/<uuid:person_id>
```

### Update

```
PUT /persons/<uuid:person_id>
```

### Delete

```
DELETE /persons/<uuid:person_id>
```

---

## 🎓 Courses

### Create

```
POST /courses/
```

```json
{
  "title": "Open Water Diver",
  "duration": "3 days",
  "price": 395
}
```

### Get all

```
GET /courses/
```

### Get one

```
GET /courses/<uuid:course_id>
```

### Update

```
PUT /courses/<uuid:course_id>
```

### Delete

```
DELETE /courses/<uuid:course_id>
```

---

## 📅 Bookings

### Create booking

```
POST /bookings/
```

```json
{
  "person_id": "UUID",
  "course_id": "UUID"
}
```

### Get all bookings

```
GET /bookings/
```

### Get one booking

```
GET /bookings/<uuid:booking_id>
```

### Delete booking

```
DELETE /bookings/<uuid:booking_id>
```

---

## 🔗 Relationships

- A **Booking** links a **Person** to a **Course**
- Validation ensures:
  - Person exists
  - Course exists

---

## 🧪 Example (curl)

```bash
curl -X POST http://localhost:5000/persons/ \
  -H "Content-Type: application/json" \
  -d '{"first_name": "Susi", "last_name": "Sonnenschein", "email": "susi@example.com"}'
```

---

## 📌 Notes

- Data is stored **in memory** (reset on restart)
- UUID validation is handled by Flask routing
- Clean separation of layers makes it easy to extend

---

## 🔮 Future Improvements

- Add PATCH endpoints
- Replace in-memory storage with PostgreSQL
- Add authentication (JWT)
- Add unit tests (pytest)
- Dockerize the application

---

## 👨‍💻 Author

Frank Hilgenberg

---

## 📄 License

Educational project
