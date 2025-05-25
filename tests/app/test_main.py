from fastapi.exceptions import HTTPException
import pytest
from src.app.main import get_user
from src.app.repo.user_repository_mock import UserRepositoryMock
from src.app.entities.user import User
from src.app.repo.transaction_history_repository_mock import TransactionsHistoryRepositoryMock
from src.app.entities.transaction_history import TransactionHistory
from src.app.repo.transaction_repository_mock import TransactionsRepositoryMock
from src.app.main import get_history
from src.app.main import post_deposit
from src.app.main import post_withdraw

class Test_Main:
    def test_get_user(self):
        repo = UserRepositoryMock()
        response = get_user()
        expected_user = {
            'name': 'Nikolas Funke',
            'agency': '1234',
            'account': '12345-6',
            'current_balance': 1000.0,
        }
        assert response == expected_user

    def test_get_histoy(self):
        repo = TransactionsHistoryRepositoryMock()
        response = get_history()
        expected_history = {
            "all_transactions": [
                {
                    'transaction_type': 'deposit',
                    'current_balance': 1000.0,
                    'ammount': 250.0,
                    'timestamp': 123456789.0
                },
                {
                    'transaction_type': 'withdraw',
                    'current_balance': 1000.0,
                    'ammount': 200.0,
                    'timestamp': 123456789.0
                },
                {
                    'transaction_type': 'deposit',
                    'current_balance': 1000.0,
                    'ammount': 500.0,
                    'timestamp': 123456789.0
                }
            ]
        }
        assert response == expected_history

    def test_post_deposit(self):
        user_repo = UserRepositoryMock()
        transaction_repo = TransactionsRepositoryMock()
        request = {
            "2": 1,
            "5": 1,
            "10": 1,
            "20": 1,
            "50": 1,
            "100": 1
        }

        response = post_deposit(request=request)
        user = user_repo.get_user(user_id=1)
        transaction = transaction_repo.get_transaction(1)
        ammount = 0
        for bill, quantity in transaction.bills.items():
            ammount += int(bill) * quantity
        user_repo.update_balance(user_id=1, ammount=ammount, transaction_type="deposit")
        expected_response = {
            'current_balance': user.current_balance,
            'timestamp': transaction_repo.get_transaction(1).timestamp,
        }
        assert response == expected_response

    def test_post_withdraw(self):
        user_repo = UserRepositoryMock()
        transaction_repo = TransactionsRepositoryMock()
        request = {
            "2": 1,
            "5": 1,
            "10": 1,
            "20": 1,
            "50": 1,
            "100": 1
        }

        response = post_withdraw(request=request)
        user = user_repo.get_user(user_id=1)
        transaction = transaction_repo.get_transaction(1)
        ammount = 0
        for bill, quantity in transaction.bills.items():
            ammount += int(bill) * quantity
        user_repo.update_balance(user_id=1, ammount=ammount, transaction_type="withdraw")
        expected_response = {
            'current_balance': user.current_balance,
            'timestamp': transaction_repo.get_transaction(1).timestamp,
        }
        assert response == expected_response
        '''    
    def test_get_item(self):
        repo = UserRepositoryMock()
        item_id = 1
        response = get_item(item_id=item_id)
        assert response == {
            'item_id' : item_id,
            'item': repo.items.get(item_id).to_dict()
        }
        
    def test_get_item_id_is_none(self):
        
        item_id = None
        with pytest.raises(HTTPException) as err:
            get_item(item_id=item_id)
    
    def test_get_item_id_is_not_int(self):
        item_id = '1'
        with pytest.raises(HTTPException) as err:
            get_item(item_id=item_id)
            
    def test_get_item_id_is_not_positive(self):
        item_id = -1
        with pytest.raises(HTTPException) as err:
            get_item(item_id=item_id)
            
    def test_create_item(self):
        repo = ItemRepositoryMock()
        
        body = {
            'item_id': 0,
            'name': 'test',
            'price': 1.0,
            'item_type': 'TOY',
            'admin_permission': False
        }
        response = create_item(request=body)
        assert response == {'item_id': 0,'item': {'admin_permission': False, 'item_type': 'TOY', 'name': 'test', 'price': 1.0}}
    
    def test_create_item_conflict(self):
        repo = ItemRepositoryMock()
        
        body = {
            'item_id': 1,
            'name': 'test',
            'price': 1.0,
            'item_type': 'TOY',
            'admin_permission': False
        }
        with pytest.raises(HTTPException) as err:
            create_item(request=body)
    
    def test_create_item_missing_id(self):
        body = {
            'name': 'test',
            'price': 1.0,
            'item_type': 'TOY',
            'admin_permission': False
        }
        with pytest.raises(HTTPException) as err:
            create_item(request=body)
        
    def test_create_item_id_is_not_int(self):
        body = {
            'item_id': '0',
            'name': 'test',
            'price': 1.0,
            'item_type': 'TOY',
            'admin_permission': False
        }
        with pytest.raises(HTTPException) as err:
            create_item(request=body)
    
    def test_create_item_id_is_not_positive(self):
        body = {
            'item_id': -1,
            'name': 'test',
            'price': 1.0,
            'item_type': 'TOY',
            'admin_permission': False
        }
        with pytest.raises(HTTPException) as err:
            create_item(request=body)
            
    def test_create_item_missing_type(self):
        body = {
            'item_id': 1,
            'name': 'test',
            'price': 1.0,
            'admin_permission': False
        }
        with pytest.raises(HTTPException) as err:
            create_item(request=body)
            
    def test_create_item_item_type_is_not_string(self):
        body = {
            'item_id': 1,
            'name': 'test',
            'price': 1.0,
            'item_type': 1,
            'admin_permission': False
        }
        with pytest.raises(HTTPException) as err:
            create_item(request=body)
            
    def test_create_item_item_type_is_not_valid(self):
        body = {
            'item_id': 1,
            'name': 'test',
            'price': 1.0,
            'item_type': 'test',
            'admin_permission': False
        }
        with pytest.raises(HTTPException) as err:
            create_item(request=body)
            
    def test_create_item_param_not_validated(self):
        body = {
            'item_id': 1,
            'name': '',
            'price': 1.0,
            'item_type': 'TOY',
            'admin_permission': False,
        }
        with pytest.raises(HTTPException) as err:
            create_item(request=body)
            
    def test_delete_item(self):
        body = {
            "item_id": 1
        }
        response = delete_item(request=body)
        assert response == {'item_id': 1, 'item': {'name': 'Barbie', 'price': 48.9, 'item_type': 'TOY', 'admin_permission': False}}
        
    def test_delete_item_missing_id(self):
        with pytest.raises(HTTPException) as err:
            delete_item(request={})
            
    def test_delete_item_id_is_not_int(self):
        body = {
            "item_id": '1'
        }
        with pytest.raises(HTTPException) as err:
            delete_item(request=body)
            
    def test_delete_item_id_not_found(self):
        body = {
            "item_id": 100
        }
        with pytest.raises(HTTPException) as err:
            delete_item(request=body)
            
    def test_delete_item_id_not_positive(self):
        body = {
            "item_id": -100
        }
        with pytest.raises(HTTPException) as err:
            delete_item(request=body)
            
    def test_delete_item_without_admin_permission(self):
        body = {
            "item_id": 4
        }
        with pytest.raises(HTTPException) as err:
            delete_item(request=body)
            
    def test_update_item(self):
        body = {
            "item_id": 2,
            "name": "test",
            "price": 1.0,
            "item_type": "TOY",
            "admin_permission": False
        }
        response = update_item(request=body)
        assert response == {'item_id': 2, 'item': {'name': 'test', 'price': 1.0, 'item_type': 'TOY', 'admin_permission': False}}
        
    def test_update_item_missing_id(self):
        body = {
            "name": "test",
            "price": 1.0,
            "item_type": "TOY",
            "admin_permission": False
        }
        with pytest.raises(HTTPException) as err:
            update_item(request=body)
    
    def test_update_item_id_is_not_int(self):
        body = {
            "item_id": "1",
            "name": "test",
            "price": 1.0,
            "item_type": "TOY",
            "admin_permission": False
        }
        with pytest.raises(HTTPException) as err:
            update_item(request=body)
            
    def test_update_item_not_positive(self):
        body = {
            "item_id": -1,
            "name": "test",
            "price": 1.0,
            "item_type": "test",
            "admin_permission": False
        }
        with pytest.raises(HTTPException) as err:
            update_item(request=body)
            
    def test_update_item_not_found(self):
        body = {
            "item_id": 1,
            "name": "test",
            "price": 1.0,
            "item_type": "test",
            "admin_permission": False
        }
        with pytest.raises(HTTPException) as err:
            update_item(request=body)
            
    def test_update_item_without_admin_permission(self):
        body = {
            "item_id": 4,
            "name": "test",
            "price": 1.0,
            "item_type": "TOY",
            "admin_permission": False
        }
        with pytest.raises(HTTPException) as err:
            update_item(request=body)
    
    def test_update_item_type_not_string(self):
        body = {
            "item_id": 1,
            "name": "test",
            "price": 1.0,
            "item_type": 1,
            "admin_permission": False
        }
        with pytest.raises(HTTPException) as err:
            update_item(request=body)
            
    def test_update_item_type_not_valid(self):
        
        body = {
            "item_id": 1,
            "name": "test",
            "price": 1.0,
            "item_type": "test",
            "admin_permission": False
        }
        with pytest.raises(HTTPException) as err:
            update_item(request=body)
            '''