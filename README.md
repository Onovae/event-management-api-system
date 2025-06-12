# 📘 Event Management API System

A FastAPI-based RESTful API that allows users to register for events, track attendance, and manage both event and speaker information. This project is designed to demonstrate CRUD operations, relationships, and basic business rules using an in-memory storage system.

---

## 🚀 Features

- ✅ Create, read, update, delete users and events
- ✅ Close event registration
- ✅ Register users for events (only if active and not already registered)
- ✅ Track attendance
- ✅ View user registrations and all registrations
- ✅ View list of speakers (pre-initialized)
- ✅ Optional: Filter users who have attended at least one event

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Pydantic**

---

## 🧩 Project Structure

event_management/
│
├── main.py
├── schemas/ # Pydantic models
│ ├── user.py
│ ├── event.py
│ ├── speaker.py
│ └── registration.py
│
├── services/ # Business logic
│ ├── user_service.py
│ ├── event_service.py
│ ├── speaker_service.py
│ └── registration_service.py
│
├── routes/ # API endpoints
│ ├── user.py
│ ├── event.py
│ ├── speaker.py
│ └── registration.py
│
└── README.md


---

## ⚙️ Requirements

- Python 3.10+
- FastAPI
- Uvicorn

You can install dependencies using:


pip install fastapi uvicorn


▶️ How to Run the App
Clone the repository


git clone https://github.com/onovae/event-management-api.git

1. cd event-management-api

2. Start the server
uvicorn main:app --reload

3. Access the API Docs

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc


📬 API Endpoints Overview
👤 Users
GET /users/

GET /users/{id}

POST /users/

PUT /users/{id}

DELETE /users/{id}

PATCH /users/{id}/deactivate

GET /users/attended (optional)

🗓️ Events
GET /events/

GET /events/{id}

POST /events/

PUT /events/{id}

DELETE /events/{id}

PATCH /events/{id}/close

🎙️ Speakers
GET /speakers/

📝 Registrations
GET /registrations/

GET /registrations/user/{user_id}

POST /registrations/

PATCH /registrations/{registration_id}/attend

🧪 Optional Feature Implemented
GET /users/attended: Lists all users who have attended at least one event.

📎 Notes
This project uses in-memory storage, which resets on app restart.

No authentication is required.

On startup, 3 speakers are preloaded into the system.

🧑‍💻 Author
Built by Maureen Onovae as part of ALTSCHOOL Examination project,

📄 License
This project is open-source and free to use under the MIT License.


