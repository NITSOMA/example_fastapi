# # import models
# from fastapi import APIRouter, Depends, status, HTTPException, Response
# from sqlalchemy.orm import Session

# from fastapi.security.oauth2 import OAuth2PasswordRequestForm

# from app import models, schemas, utils, database, oauth2


# router = APIRouter(tags=['Authentication'])


# @router.post('/login', response_model=schemas.Token)
# def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
#     # {usercredentials username}
#     # {password}
#     user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
#     if not user:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid credentials aaa')
    
#     if not utils.verify(user_credentials.password, user.password):
        
    
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Invalid credentials')
#     # create a token and return a token
#     access_token = oauth2.create_acces_token(data = {"user_id": user.id })
#     return {"access_token": access_token, "token_type": "bearer"}
    
   
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session

from app.database import get_db
from app import schemas, models, utils, oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router = APIRouter(tags=['Authentication'])


@router.post('/login')
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="invalid credentials")
    access_token = oauth2.create_acces_token(data={"user_id": user.id})
    return {"token": access_token, "token_type": "bearer"}