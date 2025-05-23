
from enum import Enum
import os

from .errors.environment_errors import EnvironmentNotFound

from .repo.item_repository_interface import IItemRepository
from .repo.user_repository_interface import IUserRepository
from .repo.transaction_repository_interface import ITransactionRepository
from .repo.transaction_history_repository_interface import ITransactionHistoryRepository


class STAGE(Enum):
    DOTENV = "DOTENV"
    DEV = "DEV"
    PROD = "PROD"
    TEST = "TEST"


class Environments:
    """
    Defines the environment variables for the application. You should not instantiate this class directly. Please use Environments.get_envs() method instead.

    Usage:

    """
    stage: STAGE

    def _configure_local(self):
        from dotenv import load_dotenv
        load_dotenv()
        os.environ["STAGE"] = os.environ.get("STAGE") or STAGE.TEST.value

    def load_envs(self):
        if "STAGE" not in os.environ or os.environ["STAGE"] == STAGE.DOTENV.value:
            self._configure_local()

        self.stage = STAGE[os.environ.get("STAGE")]

    @staticmethod
    def get_item_repo() -> IItemRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from .repo.item_repository_mock import ItemRepositoryMock
            return ItemRepositoryMock
        else:
            raise EnvironmentNotFound("STAGE")
        
    @staticmethod
    def get_user_repo() -> IUserRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from .repo.user_repository_mock import UserRepositoryMock
            return UserRepositoryMock
        else:
            raise EnvironmentNotFound("STAGE")
        
    @staticmethod
    def get_transaction_repo() -> ITransactionRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from .repo.transaction_repository_mock import TransactionsRepositoryMock
            return TransactionsRepositoryMock
        else:
            raise EnvironmentNotFound("STAGE")
        
    @staticmethod
    def get_transaction_history_repo() -> ITransactionHistoryRepository:
        if Environments.get_envs().stage ==STAGE.TEST:
            from .repo.transaction_history_repository_mock import TransactionsHistoryRepositoryMock
            return TransactionsHistoryRepositoryMock
        
        

    @staticmethod
    def get_envs() -> "Environments":
        """
        Returns the Environments object. This method should be used to get the Environments object instead of instantiating it directly.
        :return: Environments (stage={self.stage})

        """
        envs = Environments()
        envs.load_envs()
        return envs

    def __repr__(self):
        return f"Enviroments(stage={self.stage})"