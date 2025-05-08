from src.app.entities.user import User
from src.app.repo.user_repository_mock import UserRepositoryMock

if __name__ == "__main__":
    repo = UserRepositoryMock()


    user = repo.get_user()
    print(f"Usuário armazenado: {user.name} - Saldo: R${user.current_balance}")

    repo.update_balance(2000.75)
    print(f"Novo saldo: R${repo.get_user().current_balance}")
