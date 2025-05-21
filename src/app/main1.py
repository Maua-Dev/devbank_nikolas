from fastapi import FastAPI, HTTPException
from mangum import Mangum
from .environments import Environments

app = FastAPI()

user_repo = Environments.get_user_repo()()
transaction_repo = Environments.get_transaction_repo()()
transaction_history_repo = Environments.get_transaction_history_repo()()

@app.get("/")
def get_user():

    user = user_repo.get_user(1)
    if user is None:
        raise HTTPException(status_code=404, detail="User Not found")
    
    return user.to_dict()