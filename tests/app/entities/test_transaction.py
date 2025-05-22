import pytest
from src.app.entities.transaction import Transactions
from src.app.errors.entity_errors import ParamNotValidated
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.enums.bills_enum import BillsEnum

class Test_Transaction:
    def test_transaction(self):
        transaction = Transactions(
            transaction_type=TransactionTypeEnum.DEPOSIT,
            bills={
                "2": 1,
                "5": 2,
                "10": 3,
                "20": 4,
                "50": 5,
                "100": 6
            }
        )
        assert transaction.transaction_type == TransactionTypeEnum.DEPOSIT
        assert transaction.bills == {
            "2": 1,
            "5": 2,
            "10": 3,
            "20": 4,
            "50": 5,
            "100": 6
        }
    def test_transaction_dict(self):
        transaction = Transactions(
            transaction_type=TransactionTypeEnum.DEPOSIT,
            bills={
                "2": 1,
                "5": 2,
                "10": 3,
                "20": 4,
                "50": 5,
                "100": 6
            }
        )
        assert transaction.to_dict() == {
            "transaction_type": TransactionTypeEnum.DEPOSIT,
            "bills": {
                "2": 1,
                "5": 2,
                "10": 3,
                "20": 4,
                "50": 5,
                "100": 6
            }
        }
    def test_transaction_type_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transactions(
                transaction_type=None,
                bills={
                    "2": 1,
                    "5": 2
                }
            )
    def test_transaction_type_is_not_enum(self):
        with pytest.raises(ParamNotValidated):
            Transactions(
                transaction_type="DEPOSIT",
                bills={
                    "2": 1,
                    "5": 2
                }
            )

    def test_bills_is_none(self):
        with pytest.raises(ParamNotValidated):
            Transactions(
                transaction_type=TransactionTypeEnum.DEPOSIT,
                bills=["2", "5"]
            )
    def test_bills_with_invalid_value(self):
        with pytest.raises(ParamNotValidated):
            Transactions(
                transaction_type=TransactionTypeEnum.DEPOSIT,
                bills={
                    "3": 1,
                    "5": 1
                }
            )
    def test_bills_with_invalid_quantity(self):
        with pytest.raises(ParamNotValidated):
            Transactions(
                transaction_type=TransactionTypeEnum.DEPOSIT,
                bills={
                    "2": -1,
                    "5": 1
                }
            )
    def test_transaction_type_withdraw(self):
        transaction = Transactions(
            transaction_type=TransactionTypeEnum.WITHDRAW,
            bills={
                "2": 1,
                "5": 1
            }
        )
        assert transaction.transaction_type == TransactionTypeEnum.WITHDRAW

    def test_transaction_with_all_bills(self):
        transaction = Transactions(
            transaction_type=TransactionTypeEnum.DEPOSIT,
            bills={
                "2": 1,
                "5": 1,
                "10": 1,
                "20": 1,
                "50": 1,
                "100": 1,
                "200": 1
            }
        )
        assert len(transaction.bills) == 7