from typing import Dict, Optional, List
from src.app.entities.transaction import Transactions
from transaction_repository_interface import ITransactionRepository
from src.app.enums.transaction_type_enum import TransactionTypeEnum

class TransactionsRepositoryMock(ITransactionRepository):
    transactions: Dict[int, Transactions]
    def __init__(self):
        self.transactions = {
            1: Transactions(transaction_type=TransactionTypeEnum.DEPOSIT, bills={
                "1": 1,
                "5": 2,
                "10": 3,
                "20": 4,
                "50": 5,
                "100": 6
            }),
            2: Transactions(transaction_type=TransactionTypeEnum.WITHDRAW, bills={
                "1": 1,
                "5": 2,
                "10": 3,
                "20": 4,
                "50": 5,
                "100": 6
            }),
        }

    def get_all_transactions(self) -> List[Transactions]:
        return self.transactions.values()
    
    def create_transaction(self, transaction: Transactions, transaction_id: int) -> Transactions:
        transaction_id = len(self.transactions) + 1
        self.transactions[transaction_id] = transaction
        return transaction