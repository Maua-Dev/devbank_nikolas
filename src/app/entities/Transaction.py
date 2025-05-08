from datetime import datetime
from typing import Dict



class Transactions:
    timestamp: float
    current_balance: float

    def __init__(self, timestamp: float, current_balance: float, notes: Dict[int, int], trnsaction_type: str):
        self.notes = notes
        self.ammount = sum(note * qty for note, qty in notes.items())

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