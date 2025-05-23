'''from typing import Dict, Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.transaction_type_enum import TransactionTypeEnum
from ..enums.bills_enum import BillsEnum



class Transactions:
    transaction_type: TransactionTypeEnum
    bills: Dict[str, int]

    def __init__(self, transaction_type: TransactionTypeEnum=None, bills: Dict[str, int]=None):
        validation_transaction_type = self.validate_transaction_type(transaction_type)
        if validation_transaction_type[0] is False:
            raise ParamNotValidated("transaction_type", validation_transaction_type[1])
        self.transaction_type = transaction_type

        validation_bills = self.validate_bills(bills)
        if validation_bills[0] is False:
            raise ParamNotValidated("bills", validation_bills[1])
        self.bills = bills
    
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
    def validate_bills(bills: Dict[str, int]) -> Tuple[bool, str]:
        if bills is None:
            return(False, "Bills is required")
        if type(bills) != dict:
            return(False, "Bills must be a dict")
        for bill_value, quantity in bills.items():
            if bill_value not in [bill.value for bill in BillsEnum]:
                return(False, f"Invalid bill value: {bill_value}")
            if quantity < 0:
                return(False, f"Bill quantity must be positive: {quantity}")
        return(True, "")
    
    def transaction_to_dict(self) -> Dict:
        return {
            "transaction_type": self.transaction_type,
            "bills": self.bills
        }
        '''