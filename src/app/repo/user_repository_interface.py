from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.user import User

class IUserRepository(ABC):
    @abstractmethod
    def get_user(self, user_id: int) -> Optional[User]:
        """Get user by ID"""
        pass

    @abstractmethod
    def get_all_users(self) -> List[User]:
        """Get all users"""
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        """Create a new user"""
        pass

    @abstractmethod
    def update_user(self, user: User) -> User:
        """Update existing user"""
        pass

    @abstractmethod
    def update_balance(self, user_id: int, new_balance: float) -> None:
        """Update user balance"""
        pass