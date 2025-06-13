from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "Queen", "email": "queen@example.com"})
    assert response.status_code == 201
    user = response.json()
    assert user["is_active"]
    assert user["name"] == "Queen"
    assert "id" in user