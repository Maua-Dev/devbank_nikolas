from ..enums.transaction_type_enum import TransactionTypeEnum
from ..errors.entity_errors import ParamNotValidated
from typing import Tuple


class TransactionHistory:
    transaction_type: TransactionTypeEnum
    current_balance: float
    ammount: float
    timestamp: str

    def __init__(self, transaction_type: TransactionTypeEnum=None, current_balance: float=None, ammount: float=None, timestamp: str=None):
        validation_transaction_type = self.validate_transaction_type(transaction_type)
        if validation_transaction_type[0] is False:
            raise ParamNotValidated("transaction_type", validation_transaction_type[1])
        self.transaction_type = transaction_type

        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_balance", validation_current_balance[1])
        self.current_balance = current_balance

        validation_ammount = self.validate_ammount(ammount)
        if validation_ammount[0] is False:
            raise ParamNotValidated("ammount", validation_ammount[1])
        self.ammount = ammount

        validation_timestamp = self.validate_timestamp(timestamp)
        if validation_timestamp[0] is False:
            raise ParamNotValidated("timestamp", validation_timestamp[1])
        self.timestamp = timestamp

        @staticmethod
        def validate_transaction_type(transaction_type: TransactionTypeEnum) -> Tuple[bool, str]:
            if transaction_type is None:
                return(False, "Transaction is required")
            if type(transaction_type) != TransactionTypeEnum:
                return(False, "Transaction must be a TransactionTypeEnum")
            if transaction_type not in TransactionTypeEnum:
                return(False, "Transaction must be a TransactionTypeEnum")
            return(True, "")
        
        @staticmethod
        def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
            if current_balance is None:
                return(False, "Current balance is required")
            if type(current_balance) != float:
                return(False, "Current balance must be a float")
            if current_balance < 0:
                return(False, "Current balance must be greater than or equal to 0")
            return(True, "")
        
        @staticmethod
        def validate_ammount(ammount: float) -> Tuple[bool, str]:
            if ammount is None:
                return(False, "Ammount is required")
            if type(ammount) != float:
                return(False, "Ammount must be a float")
            if ammount < 0:
                return(False, "Ammount must be greater than or equal to 0")
            return(True, "")
        
        @staticmethod
        def validate_timestamp(timestamp:str) -> Tuple[bool, str]:
            if timestamp is None:
                return(False, "Timestamp is required")
            if type(timestamp) != str:
                return(False, "Timestamp must be a string")
            return(True, "")
        
        def to_dict(self) -> dict:
            return {
                "transaction_type": self.transaction_type,
                "current_balance": self.current_balance,
                "ammount": self.ammount,
                "timestamp": self.timestamp
            }
            