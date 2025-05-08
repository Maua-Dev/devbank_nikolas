from src.app.entities.user import User


class UserRepositoryMock:
    def __init__(self):
        self.user = {
            "name": "Nikolas Velho",
            "agency": "1234",
            "account": "12345-6",
            "current_balance": 1000.0
        }

    def get_user(self):
        return self.user
    
    def update_balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self.user.current_balance = new_balance
        return {"message": "Saldo atualizado com sucesso!", "new_balance": self.user.current_balance}
    