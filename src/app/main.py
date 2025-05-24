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
        "history": [
            transaction.transaction_history_to_dict() for transaction in history
        ]
    }





handler = Mangum(app, lifespan="off")
