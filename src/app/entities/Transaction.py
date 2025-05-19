from datetime import datetime
from typing import Dict
from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.transaction_type_enum import TransactionTypeEnum



class Transactions:
    transaction_type = TransactionTypeEnum
    bills: Dict[str, int]
    timestamp: str
    current_balance: float
    current_balance: float

    def __init__(self, timestamp: str=None, current_balance: float=None, bills: Dict[str, int]=None, trnsaction_type: str=None):
        self.bills = bills
        self.ammount = sum(bill * qty for bill, qty in bills.items())
        self.trnsaction_type = trnsaction_type
        if trnsaction_type == "deposit":
            self.current_balance = current_balance + self.ammount
        elif trnsaction_type == "withdraw":
            if self.ammount > current_balance:
                raise ValueError("Saldo insuficiente")
            else:
                self.current_balance = current_balance - self.ammount
        else:
            raise ValueError("Tipo de trnsação inválido")

        self.timestamp = int(datetime.timestamp(datetime.now()) * 1000)

    @staticmethod
    def validate_bills(bills: Dict[str, int]) -> Tuple[bool, str]:
        if bills is None:
            return(False, "Bills is required")
        