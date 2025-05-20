from src.app.entities.user import User
from src.app.repo.user_repository_interface import IUserRepository


class UserRepositoryMock:
    def __init__(self):
        self.user = User(
            name="Nikolas Funke",
            agency="1234",
            account="12345-6",
            current_balance=1000.0
        )

    def get_user(self) -> User:
        return self.user
    
    def create_user(self, user: User) -> User:
        self.user = user
        return self.user
    
    def update_user(self, user: User) -> User:
        self.user = user
        return self.user
    
    def set_current_balance(self, new_balance: float) -> None:
        self.user.current_balance = new_balance
        return self.user
    def get_current_balance(self) -> float:
        return self.user.current_balance
    
