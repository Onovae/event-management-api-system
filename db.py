from typing import Dict, List

# In-memory database
db: Dict[str, List[dict]] = {
    "users": [],
    "events": [],
    "speakers": [],
    "registrations": []
}

# Export access function
def get_db() -> Dict[str, List[dict]]:
    return db
