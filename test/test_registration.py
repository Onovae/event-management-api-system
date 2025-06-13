from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_user_for_event():
    user = client.post("/users/", json={"name": "Bob", "email": "bob@example.com"}).json()
    event = client.post("/events/", json={
        "title": "AI Meetup",
        "location": "Lagos",
        "date": "2025-09-20"
    }).json()

    response = client.post("/registrations/", json={
        "user_id": user["id"],
        "event_id": event["id"]
    })

    assert response.status_code == 201
    reg = response.json()
    assert reg["user_id"] == user["id"]
    assert reg["event_id"] == event["id"]
    assert reg["attended"] is False
def test_register_user_for_event_invalid_user():
    event = client.post("/events/", json={
        "title": "AI Meetup",
        "location": "Lagos",
        "date": "2025-09-20"
    }).json()

    response = client.post("/registrations/", json={
        "user_id": 9999,  # Invalid user ID
        "event_id": event["id"]
    })

    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}