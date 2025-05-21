
from enum import Enum
import os

from .errors.environment_errors import EnvironmentNotFound

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

    @staticmethod
    def get_user_repo() -> IUserRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from .repo.user_repository_mock import UserRepositoryMock
            return UserRepositoryMock
        # use "elif" conditional to add other stages
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
        return self.__dict__