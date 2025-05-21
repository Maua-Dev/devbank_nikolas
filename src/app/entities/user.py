from typing import Tuple
from ..errors.entity_errors import ParamNotValidated


class User:
    user_id: int 
    name: str
    agency: str
    account: str
    current_balance: float
    
    def __init__(self, user_id: int=None, name : str=None, agency: str=None, account: str=None, current_balance:float=None):
        validation_user_id = self.validate_user_id(user_id)
        if validation_user_id[0] is False:
            raise ParamNotValidated("user_id", validation_user_id[1])
        self.user_id = user_id

        validation_agency = self.validate_agency(agency)
        if validation_agency[0] is False:
            raise ParamNotValidated("agency", validation_agency[1])
        self.agency = agency

        validation_account = self.validate_account(account)
        if validation_account[0] is False:
            raise ParamNotValidated("Account", validation_account[1])
        self.account = account

        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_balance", validation_current_balance[1])
        self.current_balance = current_balance

        validation_name = self.validate_name(name)
        if validation_name[0] is False:
            raise ParamNotValidated("name", validation_name[1])
        self.name = name



    @staticmethod  
    def validate_agency(agency:str) -> Tuple[bool, str]:
        if agency is None:
            return(False, "Agency is required")
        if type(agency) != str:
            return(False, "Agency must be a string")
        if len(agency) != 4:
            return(False, "Agency must be 4 characters long")
        if not agency.isdigit():
            return(False< "Agency must be a number")
        return(True, "")
    
    @staticmethod
    def validate_account(account:str) -> Tuple[bool, str]:
        if account is None:
            return(False, "Account is required")
        if type(account) != str:
            return(False, "Account must be a string")
        if not account.isdigit():
            return(False, "Account must be numbers")
        parts = account.split("-")
        if len(parts) != 2:
            return(False, "Account must be in the format XXXX-X")
        if len(parts[0]) != 5:
            return(False, "Account must be im the format XXXX-X")
        if len(parts[1]) != 1:
            return(False, "Account must be in the format XXXX-X")
        return(True, "")
    
    @staticmethod
    def validate_current_balance(current_balance:float) -> Tuple[bool, str]:
        if current_balance is None:
            return(False, "Current balance is required")
        if type(current_balance) != float:
            return(False, "Current balance must be a float")
        if current_balance < 0:
            return(False, "Current balance must be a positive number")
        return(True, "")

    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return(False, "Name is required")
        if type(name) != str:
            return(False, "Name must be a string")
        if len(name) < 3:
            return(False, "Name must be at least 3 characters long")
        return(True, "")

    @staticmethod
    def validate_user_id(user_id: int) -> Tuple[bool, str]:
        if user_id is None:
            return (False, "User ID is required")
        if type(user_id) != int:
            return (False, "User ID must be an integer")
        if user_id < 0:
            return (False, "User ID must be a positive number")
        return (True, "")

    def to_dict(self) -> dict:
        return {
            'user_id': self.user_id,
            'name': self.name, 
            'agency': self.agency,
            'account': self.account,
            'current_balance': self.current_balance
        }

