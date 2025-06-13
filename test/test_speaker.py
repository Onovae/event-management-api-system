from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_speakers():
    response = client.get("/speakers/")
    assert response.status_code == 200
    speakers = response.json()
    assert isinstance(speakers, list)
    assert len(speakers) == 3
    assert all("name" in speaker for speaker in speakers)
def test_get_speaker_by_id():
    response = client.get("/speakers/1")
    assert response.status_code == 200
    speaker = response.json()
    assert speaker["name"] == "John Doe"
    assert speaker["id"] == 1
def test_get_speaker_by_invalid_id():
    response = client.get("/speakers/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Speaker not found"}