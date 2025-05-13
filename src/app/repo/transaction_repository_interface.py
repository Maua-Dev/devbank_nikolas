from abc import ABC, abstractmethod
from typing import List, Optional, Dict
from src.app.entities.transaction import Transactions


class ITransactionRepository(ABC):
    @abstractmethod
    def get_all_transactions(self) -> List[Transactions]:
        pass

    @abstractmethod
    def get_transaction(self, transaction_id: int) -> Optional[Transactions]:
        pass

    @abstractmethod
    def create_transaction(self, transaction: Transactions, transaction_id: int) -> Transactions:
        pass

    @abstractmethod
    def delete_transaction(self, transaction_id: int) -> Optional[Transactions]:
        pass

    @abstractmethod
    def update_transaction(
        self,
        bills: Optional[Dict[str, int]] = None,
        current_balance: Optional[float] = None,
        trnsaction_type: Optional[str] = None
    ) -> Optional[Transactions]:
        pass
