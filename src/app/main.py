from fastapi import FastAPI, HTTPException
from mangum import Mangum
from .environments import Environments
from .entities.user import User
from .errors.entity_errors import ParamNotValidated

app = FastAPI()

in_use_id = 1
user_repo = Environments.get_user_repo()()

@app.get("/")
def get_user():
    user = user_repo.get_user(user_id=in_use_id)
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user.to_dict()



handler = Mangum(app, lifespan="off")
