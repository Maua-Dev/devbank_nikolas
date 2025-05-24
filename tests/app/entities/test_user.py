import pytest
from src.app.entities.user import User
from src.app.errors.entity_errors import ParamNotValidated

class Test_User:
    def test_user(self):
        user = User(1, "Joao", "1234", "12345-6", 1000.0)
        assert user.name == "Joao"
        assert user.agency == "1234"
        assert user.account == "12345-6"
        assert user.current_balance == 1000.0
        assert user.user_id == 1

    def test_user_dict(self):
        user = User(1, "Joao", "1234", "12345-6", 1000.0)
        assert user.user_to_dict() == {
            'name': 'Joao',
            'agency': '1234',
            'account': '12345-6',
            'current_balance': 1000.0
        }

    def test_user_id_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(user_id=None, name="Joao", agency="1234", account="12345-6", current_balance=1000.0)
    def test_user_id_is_not_int(self):
        with pytest.raises(ParamNotValidated):
            User(user_id="1", name="Joao", agency="1234", account="12345-6", current_balance=1000.0)
    def test_user_id_is_negative(self):
        with pytest.raises(ParamNotValidated):
            User(user_id=-1, name="Joao", agency="1234", account="12345-6", current_balance=1000.0)

    def test_user_agency_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(user_id=1, name="Joao", agency=None, account="12345-6", current_balance=1000.0)
    def test_user_agency_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            User(user_id=1, name="Joao", agency=1234, account="12345-6", current_balance=1000.0)
    def test_user_agency_is_too_short(self):
        with pytest.raises(ParamNotValidated):
            User(user_id=1, name="Joao", agency="123", account="12345-6", current_balance=1000.0)
    def test_user_agency_is_too_long(self):
        with pytest.raises(ParamNotValidated):
            User(user_id=1, name="Joao", agency="12345", account="12345-6", current_balance=1000.0)
    def test_user_agency_is_not_number(self):
        with pytest.raises(ParamNotValidated):
            User(user_id=1, name="Joao", agency="1234a", account="12345-6", current_balance=1000.0)
    
    def test_user_account_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(user_id=1, name="Joao", agency="1234", account=None, current_balance=1000.0)
    def test_user_account_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            User(user_id=1, name="Joao", agency="1234", account=12345, current_balance=1000.0)
    def test_user_account_is_too_short(self):
        with pytest.raises(ParamNotValidated):
            User(user_id=1, name="Joao", agency="1234", account="1234", current_balance=1000.0)
    def test_user_account_is_too_long(self):
        with pytest.raises(ParamNotValidated):
            User(user_id=1, name="Joao", agency="1234", account="123456", current_balance=1000.0)
    def test_user_account_is_not_number(self):
        with pytest.raises(ParamNotValidated):
            User(user_id=1, name="Joao", agency="1234", account="12345a", current_balance=1000.0)
    def test_user_account_is_not_valid_format(self):
        with pytest.raises(ParamNotValidated):
            User(user_id=1, name="Joao", agency="1234", account="12345-67-8", current_balance=1000.0)
    
    def test_user_current_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(user_id=1, name="Joao", agency="1234", account="12345-6", current_balance=None)
    def test_user_current_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            User(user_id=1, name="Joao", agency="1234", account="12345-6", current_balance="1000.0")
    def test_user_current_balance_is_negative(self):
        with pytest.raises(ParamNotValidated):
            User(user_id=1, name="Joao", agency="1234", account="12345-6", current_balance=-1000.0)
    
    def test_user_name_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(user_id=1, name=None, agency="1234", account="12345-6", current_balance=1000.0)
    def test_user_name_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            User(user_id=1, name=1234, agency="1234", account="12345-6", current_balance=1000.0)
    def test_user_name_is_too_short(self):
        with pytest.raises(ParamNotValidated):
            User(user_id=1, name="Jo", agency="1234", account="12345-6", current_balance=1000.0)
    