from abc import ABC, abstractmethod
from typing import List, Optional, Tuple
from ..entities.transaction_history import TransactionHistory

class ITransactionHistoryRepository(ABC):
    @abstractmethod
    def get_all_transactions(self) -> List[TransactionHistory]:
        pass
    @abstractmethod
    def create_transaction(self, transaction: TransactionHistory):
        pass