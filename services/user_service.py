from typing import List, Optional
from uuid import uuid4, UUID

from schemas.user import User, UserCreate, UserUpdate
from db import get_db

def get_users() -> List[User]:
    return [User(**user) for user in get_db()["users"]]

def get_user(user_id: UUID) -> Optional[User]:
    return next(
        (User(**u) for u in get_db()["users"] if str(u["id"]) == str(user_id)),
        None
    )

def create_user(user_data: UserCreate) -> User:
    db = get_db()
    new_user = User(id=uuid4(), is_active=True, **user_data.model_dump())
    db["users"].append(new_user.model_dump())
    return new_user

def update_user(user_id: UUID, user_data: UserUpdate) -> Optional[User]:
    user = get_user(user_id)
    if not user:
        return None

    update_data = user_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user, key, value)

    db = get_db()
    for i, u in enumerate(db["users"]):
        if str(u["id"]) == str(user_id):
            db["users"][i] = user.model_dump()
            break
    return user

def delete_user(user_id: UUID) -> bool:
    db = get_db()
    before = len(db["users"])
    db["users"] = [u for u in db["users"] if str(u["id"]) != str(user_id)]
    return len(db["users"]) < before

def deactivate_user(user_id: UUID) -> Optional[User]:
    user = get_user(user_id)
    if not user:
        return None

    user.is_active = False
    db = get_db()
    for i, u in enumerate(db["users"]):
        if str(u["id"]) == str(user_id):
            db["users"][i] = user.model_dump()
            break
    return user
