import pytest
from src.app.entities.transaction_history import TransactionHistory
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.errors.entity_errors import ParamNotValidated

class Test_TransactionHistory:
    def test_transaction_history(self):
        transaction = TransactionHistory(
            transaction_type=TransactionTypeEnum.DEPOSIT,
            current_balance=1000.0,
            ammount=500.0,
            timestamp="2024-01-01 10:00:00"
        )
        assert transaction.transaction_type == TransactionTypeEnum.DEPOSIT
        assert transaction.current_balance == 1000.0
        assert transaction.ammount == 500.0
        assert transaction.timestamp == "2024-01-01 10:00:00"
    
    def test_transaction_history_dict(self):
        transaction = TransactionHistory(
            transaction_type=TransactionTypeEnum.DEPOSIT,
            current_balance=1000.0,
            ammount=500.0,
            timestamp="2024-01-01 10:00:00"
        )
        assert transaction.transaction_history_to_dict() == {
            "transaction_type": TransactionTypeEnum.DEPOSIT,
            "current_balance": 1000.0,
            "ammount": 500.0,
            "timestamp": "2024-01-01 10:00:00"
        }

    def test_transaction_type_is_none(self):
        with pytest.raises(ParamNotValidated):
            TransactionHistory(
                transaction_type=None,
                current_balance=1000.0,
                ammount=500.0,
                timestamp="2024-01-01 10:00:00"
            )

    def test_transaction_type_is_not_enum(self):
        with pytest.raises(ParamNotValidated):
            TransactionHistory(
                transaction_type="DEPOSIT",
                current_balance=1000.0,
                ammount=500.0,
                timestamp="2024-01-01 10:00:00"
            )

    def test_current_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            TransactionHistory(
                transaction_type=TransactionTypeEnum.DEPOSIT,
                current_balance=None,
                ammount=500.0,
                timestamp="2024-01-01 10:00:00"
            )

    def test_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            TransactionHistory(
                transaction_type=TransactionTypeEnum.DEPOSIT,
                current_balance="1000.0",
                ammount=500.0,
                timestamp="2024-01-01 10:00:00"
            )

    def test_current_balance_is_negative(self):
        with pytest.raises(ParamNotValidated):
            TransactionHistory(
                transaction_type=TransactionTypeEnum.DEPOSIT,
                current_balance=-1000.0,
                ammount=500.0,
                timestamp="2024-01-01 10:00:00"
            )

    def test_ammount_is_none(self):
        with pytest.raises(ParamNotValidated):
            TransactionHistory(
                transaction_type=TransactionTypeEnum.DEPOSIT,
                current_balance=1000.0,
                ammount=None,
                timestamp="2024-01-01 10:00:00"
            )

    def test_ammount_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            TransactionHistory(
                transaction_type=TransactionTypeEnum.DEPOSIT,
                current_balance=1000.0,
                ammount="500.0",
                timestamp="2024-01-01 10:00:00"
            )

    def test_ammount_is_negative(self):
        with pytest.raises(ParamNotValidated):
            TransactionHistory(
                transaction_type=TransactionTypeEnum.DEPOSIT,
                current_balance=1000.0,
                ammount=-500.0,
                timestamp="2024-01-01 10:00:00"
            )

    def test_timestamp_is_none(self):
        with pytest.raises(ParamNotValidated):
            TransactionHistory(
                transaction_type=TransactionTypeEnum.DEPOSIT,
                current_balance=1000.0,
                ammount=500.0,
                timestamp=None
            )

    def test_timestamp_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            TransactionHistory(
                transaction_type=TransactionTypeEnum.DEPOSIT,
                current_balance=1000.0,
                ammount=500.0,
                timestamp=123
            )