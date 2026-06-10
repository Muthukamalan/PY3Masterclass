from typing import Optional, Sequence
from sqlalchemy.orm import Session
from app.models.users import User
from app.schemas.users import (
    UserCreate,
    UserUpdate,
    UserResponse,
)
from app.repository.base import UserRepository
from datetime import datetime, timezone


class UserSQLiteRepository(UserRepository):
    """Repository for User database operations"""

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserCreate) -> User:
        """Create a new user"""
        db_user = User(
            name=user.name,
            email=user.email,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user(self, user_id: int) -> Optional[User]:
        """Get user by ID"""
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        return self.db.query(User).filter(User.email == email).first()

    def get_users(
        self, skip: int = 0, limit: int = 100
    ) -> tuple[Sequence[UserResponse], int]:
        """Get all users with pagination"""
        total = self.db.query(User).count()
        users = self.db.query(User).offset(skip).limit(limit).all()
        return users, total

    def update_user(self, user_id: int, user: UserUpdate) -> Optional[User]:
        """Update user by ID"""
        db_user = self.get_user(user_id)
        if db_user:
            update_data = user.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_user, key, value)
            self.db.commit()
            self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int) -> bool:
        """Delete user by ID"""
        db_user = self.get_user(user_id)
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
            return True
        return False
