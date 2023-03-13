import config
from pytz import timezone
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import TypeVar, Generic

from fastapi import Depends
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.http import HTTPBearer, HTTPAuthorizationCredentials

T = TypeVar('T')

class BaseRepo():
    @staticmethod
    async def retrieve_all(db: Session, model: Generic[T]):
        return db.query(model).all()
    
    @staticmethod
    async def retrieve_by_id(db: Session, model: Generic[T], id: int):
        return db.query(model).filter(model.id == id).all()
    
    @staticmethod
    async def insert(db: Session, model: Generic[T]):
        db.add(model)
        db.commit()
        db.refresh()
    
    @staticmethod
    async def update(db: Session, model: Generic[T]):
        db.commit()
        db.refresh()
    
    @staticmethod
    async def delete(db: Session, model: Generic[T]):
        db.delete(model)
        db.commit()
        db.refresh()

class UsersRepo(BaseRepo):
    
    @staticmethod
    async def find_by_username(db: Session, model: Generic[T], username: str):
        return db.query(model).filter(model.username == username).all()
    
class JWTRepo():
    
    @staticmethod
    def generate_token(data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        expire = datetime.now(timezone(config.TIMEZONE)) + expires_delta if expires_delta is not None else timedelta(minutes=config.ACCESS_TOKEN_EXPIRATION_MINUTES)
        to_encode.update({"exp": expire})
        encode_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
        return encode_jwt
    
    @staticmethod
    def decode_token(token: str):
        try:
            decode_token = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
            return decode_token if decode_token["expires"] >= datetime.time() else None
        except JWTError:
            return None
        
class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)
        
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials| HTTPException:
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        
        if credentials:
            if not credentials.schema == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authorization code.")
            if self.verify_jwt(credentials.credentials):
                raise Exception(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")
            
        
    def verify_jwt(self, jwt_token: str):
        
        try:
            payload = jwt.decode(jwt_token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        except JWTError:
            payload = None
            
        if payload:
            return True
        return False
            
    