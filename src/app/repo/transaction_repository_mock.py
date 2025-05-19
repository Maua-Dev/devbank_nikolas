from typing import Dict, Optional, List
from src.app.entities.transaction import Transactions
from transaction_repository_interface import ITransactionRepository


class TransactionsRepositoryMock(ITransactionRepository):
    transactions: Dict[int, Transactions]

    def __init__(self):
        self.transactions = {
            1: Transactions(timestamp=0, current_balance=1000.0, bills={"10": 1, "50": 1}, trnsaction_type="deposit"),
            2: Transactions(timestamp=0, current_balance=1060.0, bills={"20": 3}, trnsaction_type="withdraw")
        }

    def get_all_transactions(self) -> List[Transactions]:
        return list(self.transactions.values())

    def get_transaction(self, transaction_id: int) -> Optional[Transactions]:
        return self.transactions.get(transaction_id, None)

    def create_transaction(self, transaction: Transactions, transaction_id: int) -> Transactions:
        self.transactions[transaction_id] = transaction
        return transaction

    def delete_transaction(self, transaction_id: int) -> Optional[Transactions]:
        return self.transactions.pop(transaction_id, None)

    def update_transaction(
        self,
        transaction_id: int,
        bills: Optional[Dict[str, int]] = None,
        current_balance: Optional[float] = None,
        trnsaction_type: Optional[str] = None
    ) -> Optional[Transactions]:
        transaction = self.transactions.get(transaction_id)
        if not transaction:
            return None

        if bills is not None:
            transaction.bills = bills
            transaction.ammount = sum(int(k) * v for k, v in bills.items())

        if current_balance is not None:
            transaction.current_balance = current_balance

        if trnsaction_type is not None:
            if trnsaction_type not in ["deposit", "withdraw"]:
                raise ValueError("Tipo de transação inválido")
            transaction.trnsaction_type = trnsaction_type

        self.transactions[transaction_id] = transaction
        return transaction
