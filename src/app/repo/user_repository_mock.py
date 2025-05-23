from ..entities.user import User
from ..repo.user_repository_interface import IUserRepository
from typing import List, Optional
from ..errors.entity_errors import ParamNotValidated



class UserRepositoryMock(IUserRepository):
    def __init__(self):
        self.users = {
            1: User(user_id=1, name="Nikolas Funke", agency="1234", account="12345-6", current_balance=1000.0),
            2: User(user_id=2, name="Rodrigo Trigo", agency="1212", account="98765-4", current_balance=1000.0)
        }

    def get_user(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id, None)
    
    def get_all_users(self) -> List[User]:
        return list(self.users.values())
    
    def create_user(self, user: User) -> User:
        if user.user_id in self.users:
            raise ParamNotValidated("user_id", "User ID already exists")
        self.users[user.user_id] = user
        return user
    
    def update_user(self, user: User) -> User:
        if user.user_id not in self.users:
            raise ParamNotValidated("user_id", "User not found")
        self.users[user.user_id] = user
        return user

    def update_balance(self, user_id: int, new_balance: float) -> None:
        user = self.get_user(user_id)
        if user is None:
            raise ParamNotValidated("user_id", "User not found")
        user.current_balance = new_balance

