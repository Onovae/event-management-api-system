from fastapi import FastAPI
from uuid import UUID, uuid4
from typing import Dict, List
from routes import user, event, speaker, registration
from db import get_db

app = FastAPI(title="Event Management API System")


# Initialize with 3 predefined speakers
def initialize_speakers():
    initial_speakers = [
        {
            "id": "d5cfdbcb-dc6d-4d78-a4db-a7a50d9b8790",
            "name": "Maureen Johnson",
            "topic": "The Future of AI Agents"
        },
        {
            "id": "28f8cc0a-a5e4-4796-bd84-a74764f475f0",
            "name": "Rotimi Smith",
            "topic": "Cybersecurity Challenges"
        },
        {
            "id": "7a410697-a848-4ffc-a634-bf401db8467d",
            "name": "Clara Onovae",
            "topic": "Cloud Computing Strategies"
        }
    ]
    get_db()["speakers"].extend(initial_speakers)

initialize_speakers()

# Include routers (to be implemented in the routes/)
app.include_router(user.router)
app.include_router(event.router)
app.include_router(speaker.router)
app.include_router(registration.router)



