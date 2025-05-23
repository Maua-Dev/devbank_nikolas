from fastapi import FastAPI, HTTPException
from mangum import Mangum
from app.environments import Environments
from .repo.user_repository_mock import UserRepositoryMock

app = FastAPI()

user_repo = Environments.get_user_repo()()
transaction_repo = Environments.get_transaction_repo()()
transaction_history_repo = Environments.get_transaction_history_repo()()

@app.get("/")
def get_user():

    user = UserRepositoryMock.get_user(1)
    if user is None:
        raise HTTPException(status_code=404, detail="User Not found")
    
    return user.user_to_dict()

handler = Mangum(app, lifespan="off")
