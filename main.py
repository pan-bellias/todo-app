import imp
from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy.orm.session import Session

from database import get_db
from models import User
from schemas import UserCreate
import crud

app = FastAPI()

@app.post("/api/users", response_model=User)
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    """add new user"""
    user = crud.get_user_by_email(db, user_data.email)
    if user:
        raise HTTPException(status_code=409,
   	                    detail="Email already registered.")
    signedup_user = crud.create_user(db, user_data)
    return signedup_user