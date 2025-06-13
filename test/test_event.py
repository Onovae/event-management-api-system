from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_event():
    response = client.post("/events/", json={
        "title": "Tech Insight africa",
        "location": "Virtual",
        "date": "2025-12-01"
    })
    assert response.status_code == 201
    event = response.json()
    assert event["title"] == "Tech Insight africa"
    assert event["is_open"]
