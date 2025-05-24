from typing import Dict, Optional, List
from ..entities.transaction_history import TransactionHistory
from .transaction_history_repository_interface import ITransactionHistoryRepository
from ..enums.transaction_type_enum import TransactionTypeEnum

class TransactionsHistoryRepositoryMock(ITransactionHistoryRepository):
    transactions_history: List[TransactionHistory]
    
    def __init__(self):
        self.transactions_history = [
            TransactionHistory(
                transaction_type= TransactionTypeEnum.DEPOSIT,
                current_balance=1000.0,
                ammount = 250.0,
                timestamp = "2024-01-01 10:00:00"
            ),
            TransactionHistory(
                transaction_type = TransactionTypeEnum.WITHDRAW,
                current_balance = 1000.0,
                ammount = 200.0,
                timestamp = "2024-01-01 10:00:00"
            ),
            TransactionHistory(
                transaction_type = TransactionTypeEnum.DEPOSIT,
                current_balance = 1000.0,
                ammount = 500.0,
                timestamp = "2024-01-01 10:00:00"
            )
        ]

    def get_transactions_history(self) -> List[TransactionHistory]:
        return self.transactions_history
    
    def create_transaction(self, transactions_history: TransactionHistory) -> None:
        self.transactions_history.append(transactions_history)
        return None