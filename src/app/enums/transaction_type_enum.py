from enum import Enum

class TransactionTypeEnum(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"