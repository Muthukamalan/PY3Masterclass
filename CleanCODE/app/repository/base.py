from abc import ABC, abstractmethod
from typing import Optional, Sequence
from app.models.users import User
from app.schemas.users import UserCreate, UserResponse, UserUpdate


class UserRepository(ABC):
    """Abstract base class for User repository"""

    @abstractmethod
    def create_user(self, user: UserCreate) -> User:
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> UserResponse:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def get_users(
        self, skip: int = 0, limit: int = 100
    ) -> tuple[Sequence[UserResponse], int]:
        pass

    @abstractmethod
    def update_user(self, user_id: int, user: UserUpdate) -> Optional[User]:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        pass
