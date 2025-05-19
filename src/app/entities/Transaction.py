from datetime import datetime
from typing import Dict
from typing import Tuple
from ..errors.entity_errors import ParamNotValidated




class Transactions:
    timestamp: float
    current_balance: float

    def __init__(self, timestamp: float=None, current_balance: float=None, bills: Dict[int, int]=None, trnsaction_type: str=None):
        self.bills = bills
        self.ammount = sum(note * qty for note, qty in bills.items())

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