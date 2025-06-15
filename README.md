# 📘 Event Management API System

A FastAPI-based REST API to manage users, events, speakers, and registrations. The system uses in-memory storage with UUID-based identifiers, and supports full CRUD operations, attendance tracking, and validation rules.

---

## 🚀 Features

- ✅ Create, read, update, delete (CRUD) users, events, and registrations
- ✅ Automatically initialize with 3 speakers
- ✅ Register users for events (only once, only if active, and only for open events)
- ✅ Track event attendance
- ✅ Deactivate users
- ✅ Close event registration
- ✅ Retrieve users who attended at least one event
- 🔒 No authentication required
- ⚙️ Data is stored in in-memory dictionaries/lists (no database required)

---

## 📦 Tech Stack

- **FastAPI**
- **Pydantic v2**
- **Uvicorn** (for development server)

---

## 🗂️ Project Structure

.
├── main.py
├── db.py
├── schemas/
│ ├── user.py
│ ├── event.py
│ ├── speaker.py
│ └── registration.py
├── services/
│ ├── user_service.py
│ ├── event_service.py
│ ├── speaker_service.py
│ └── registration_service.py
├── routes/
│ ├── user.py
│ ├── event.py
│ ├── speaker.py
│ └── registration.py
├── requirements.txt
└── README.md

---

## ⚙️ Requirements

- Python 3.10+
- FastAPI
- Uvicorn

---

## ▶️ Getting Started

### 🔧 Install Dependencies

```bash
python -m venv venv

source venv/bin/activate  # or `venv\Scripts\activate` on Windows

pip install -r requirements.txt

pip install fastapi uvicorn


▶️ How to Run the App

Clone the repository

```bash
git clone https://github.com/onovae/event-management-api.git

cd event-management-api-system

# Start the server
uvicorn main:app --reload

# Access the API Docs

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc


📬 API Endpoints Overview

👤 Users
| Method   | Endpoint                      | Description             |
| -------- | ----------------------------- | ----------------------- |
| `GET`    | `/users/`                     | Get all users           |
| `POST`   | `/users/`                     | Create a user           |
| `GET`    | `/users/{user_id}`            | Get a specific user     |
| `PUT`    | `/users/{user_id}`            | Update a user           |
| `DELETE` | `/users/{user_id}`            | Delete a user           |
| `PATCH`  | `/users/{user_id}/deactivate` | Deactivate a user       |
| `GET`    | `/users/attended`             | List users who attended |


🗓️ Events
| Method   | Endpoint                          | Description              |
| -------- | --------------------------------- | ------------------------ |
| `GET`    | `/events/`                        | Get Events               |
| `POST`   | `/events/`                        | Create Event             |
| `GET`    | `/events/{event_id}`              | Get Event                |
| `PUT`    | `/events/{event_id}`              | Update Event             |
| `DELETE` | `/events/{event_id}`              | Delete Event             |
| `PATCH`  | `/events/{event_id}/close`        | Close Event              |
| `GET`    | `/events/by-speaker/{speaker_id}` | Get Events by Speaker |


🎤 Speakers
| Method | Endpoint                 | Description            |
| ------ | ------------------------ | ---------------------- |
| `GET`  | `/speakers/`             | Get all speakers       |
| `GET`  | `/speakers/{speaker_id}` | Get a specific speaker |


📝 Registrations
| Method  | Endpoint                                  | Description                  |
| ------- | ----------------------------------------- | ---------------------------- |
| `GET`   | `/registrations/`                         | List all registrations       |
| `POST`  | `/registrations/`                         | Register a user for an event |
| `PATCH` | `/registrations/{registration_id}/attend` | Mark attendance              |
| `GET`   | `/registrations/user/{user_id}`           | Get registrations for a user |

```

### 📎Notes

This project uses in-memory storage, which resets on app restart.

No authentication is required.

#### 🎤 Predefined Speakers

On startup, 3 speakers are preloaded into the system.

The application starts with 3 speakers. Use `GET /speakers/` to view them. Example:

UUIDs are used as unique identifiers across all resources.

All endpoints return appropriate status codes.

Error handling is implemented for not found, inactive users, and duplicate registrations.

🧑‍💻 Author
Built by Maureen Onovae as part of ALTSCHOOL Second Semester Examination project,

📄 License
This project is open-source and free to use under the MIT License.



These versions reflect Pydantic v2 compatibility and email-validator required for EmailStr.



