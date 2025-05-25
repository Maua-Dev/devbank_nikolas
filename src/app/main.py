from fastapi import FastAPI, HTTPException
from mangum import Mangum
from .environments import Environments
from .repo.user_repository_mock import UserRepositoryMock
from .repo.transaction_repository_mock import TransactionsRepositoryMock

app = FastAPI()

user_repo = Environments.get_user_repo()()
transaction_repo = Environments.get_transaction_repo()()
transaction_history_repo = Environments.get_transaction_history_repo()()

in_user_id = 1

@app.get("/")
def get_user():


    user = user_repo.get_user(user_id=in_user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User Not found")
    
    return user.user_to_dict()

@app.get("/history")
def get_history():
    history = transaction_history_repo.get_transactions_history()
    if history is None:
        raise HTTPException(status_code=404, detail="History Not found")
    
    return {
        "all_transactions": [
            transaction.transaction_history_to_dict() for transaction in history
        ]
    }

@app.post("/deposit")
def post_deposit(request: dict):

    ammount = 0
    transaction = transaction_repo.get_transaction(1)
    user = user_repo.get_user(user_id=in_user_id)
    request = transaction.bills

    for bill, quantity in transaction.bills.items():
        ammount += int(bill) * quantity
    if ammount is None:
        raise HTTPException(status_code=404, detail="Transaction Not found")
    elif ammount < 0:
        raise HTTPException(status_code=400, detail="Transaction is negative")
    elif ammount > 2 * user.current_balance:
        raise HTTPException(status_code=400, detail="Transaction is greater than 2x the current balance")
    else:
        user_repo.update_balance(user_id=in_user_id, ammount=ammount, transaciton_type="deposit")
        return {
            "current_balance": user.current_balance,
            "timestamp": transaction.timestamp,
        }


handler = Mangum(app, lifespan="off")
