from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from sqlalchemy.orm import Session
from app.repository.users import UserSQLiteRepository
from app.schemas.users import UserCreate, UserResponse, UserUpdate, UserListResponse
from app.database.db import get_db
from app.services.users import UserService


user_router = APIRouter(prefix="/users", tags=["users"])


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repository = UserSQLiteRepository(db)
    return UserService(repository)


# 2. The clean, reusable type alias
UserServiceDep = Annotated[UserService, Depends(get_user_service)]


@user_router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, usr_srv: UserServiceDep) -> UserResponse:
    """Get user by ID"""
    return usr_srv.GetUser(user_id)


@user_router.get("/", response_model=UserListResponse)
def get_users(
    usr_srv: UserServiceDep, skip: int = 0, limit: int = 100
) -> UserListResponse:
    """Get all users with pagination"""
    return usr_srv.GetUsers(skip, limit)


@user_router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, usr_srv: UserServiceDep) -> UserResponse:
    """Create a new user"""
    return usr_srv.CreateUser(user)


@user_router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int, user: UserUpdate, usr_srv: UserServiceDep
) -> UserResponse:
    """Update user by ID"""
    updated_user = usr_srv.UpdateUser(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user


@user_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, usr_srv: UserServiceDep) -> None:
    """Delete user by ID"""
    success = usr_srv.DeleteUser(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
