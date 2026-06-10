from typing import Optional
from app.repository import UserRepository
from app.schemas.users import UserCreate, UserUpdate, UserResponse, UserListResponse


class UserService:
    """Service layer for user-related business logic and Validation comes here"""
    def __init__(self, repository: UserRepository) -> None:
        self.repo: UserRepository = repository

    def CreateUser(self, user: UserCreate) -> UserResponse:
        return self.repo.create_user(user)

    def GetUser(self, user_id: int) -> UserResponse:
        return self.repo.get_user(user_id)

    def GetUsers(self, skip: int = 0, limit: int = 100) -> UserListResponse:
        users, total = self.repo.get_users(skip, limit)
        return UserListResponse(data=users, total=total)

    def UpdateUser(self, user_id: int, user: UserUpdate) -> Optional[UserResponse]:
        return self.repo.update_user(user_id, user)

    def DeleteUser(self, user_id: int) -> bool:
        return self.repo.delete_user(user_id)
