from typing import Dict, Optional, List
from ..entities.Transaction import Transactions
from .transaction_repository_interface import ITransactionRepository
from ..enums.transaction_type_enum import TransactionTypeEnum

class TransactionsRepositoryMock(ITransactionRepository):
    transactions: Dict[int, Transactions]
    def __init__(self):
        self.transactions = {
            1: Transactions(transaction_type=TransactionTypeEnum.DEPOSIT, bills={
                "2": 1,
                "5": 1,
                "10": 1,
                "20": 1,
                "50": 1,
                "100": 1
            }, timestamp=123456789.0),
            2: Transactions(transaction_type=TransactionTypeEnum.WITHDRAW, bills={
                "2": 1,
                "5": 1,
                "10": 1,
                "20": 1,
                "50": 1,
                "100": 1
            }, timestamp=123456789.0),
        }

    def get_all_transactions(self) -> List[Transactions]:
        return self.transactions.values()
    
    def create_transaction(self, transaction: Transactions, transaction_id: int) -> Transactions:
        self.transactions[transaction_id] = transaction
        return transaction
    
    def get_transaction(self, transaction_id: int) -> Optional[Transactions]:
        return self.transactions.get(transaction_id, None)
    
    