from fastapi import FastAPI
from uuid import UUID, uuid4
from typing import Dict, List
from routes import user, event, speaker, registration
from db import get_db

app = FastAPI(title="Event Management API System")


# Initialize with 3 default speakers
def initialize_speakers():
    speakers = [
        {"id": str(uuid4()), "name": "Maureen Johnson", "topic": "The Future of AI Agents"},
        {"id": str(uuid4()), "name": "Bob Onovae", "topic": "Cybersecurity Trends"},
        {"id": str(uuid4()), "name": "Carol Kennedy", "topic": "Cloud Computing"}
    ]
    get_db()["speakers"].extend(speakers)

initialize_speakers()

# Include routers (to be implemented in the routes/)
app.include_router(user.router)
app.include_router(event.router)
app.include_router(speaker.router)
app.include_router(registration.router)



