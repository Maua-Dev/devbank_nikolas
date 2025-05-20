from abc import ABC, abstractmethod
from typing import List, Optional, Dict
from src.app.entities.transaction import Transactions


class ITransactionRepository(ABC):
    @abstractmethod
    def get_all_transactions(self) -> List[Transactions]:
        pass

    @abstractmethod
    def create_transaction(self, transaction: Transactions, transaction_id: int) -> Transactions:
        pass
