from abc import ABC, abstractmethod
from typing import List, Optional
from src.app.entities.user import User

class IUserRepository(ABC):
    @abstractmethod
    def get_user(self) -> User:
        pass
    @abstractmethod
    def create_user(self, user: User) -> User:
        pass
    @abstractmethod
    def update_user(self, user: User) -> User:
        pass
    @abstractmethod    
    def get_current_balance(self, current_balance: float) -> float:
        pass
    @abstractmethod
    def set_current_balance(self, new_balance: float) -> None:
        pass