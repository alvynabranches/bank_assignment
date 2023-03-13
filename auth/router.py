import config
from db import get_db
from models import Users
from pytz import timezone
from fastapi import Depends
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi.routing import APIRouter
from passlib.context import CryptContext
from repository import JWTRepo, JWTBearer, UsersRepo
from schemas import RequestSchema, ResponseSchema, TokenResponse

route = APIRouter()
pwd_context = CryptContext(schemes=["bcrpyt"], deprecated="auto")

@route.post("/signup")
async def signup(request: RequestSchema, db: Session = Depends(get_db)):
    try:
        _user = Users(
            username=request.parameter.data["username"],
            password=pwd_context.hash(request.parameter.data["password"]),
            email=request.parameter.data["email"],
            phone=request.parameter.data["phone"],
            first_name=request.parameter.data["first_name"],
            last_name=request.parameter.data["last_name"],
            create_date=datetime.now(timezone(config.TIMEZONE))
        )
        await UsersRepo.insert(db, _user)
        return ResponseSchema(code=201, status="Created", message="Created successfully!").dict(exclude_none=True)
    except Exception as e:
        print(e.args)
        return ResponseSchema(code=500, status="Internal Server Error", message="Internal Server Error").dict(exclude_none=True)

@route.post("/login")
async def login(request: RequestSchema, db: Session = Depends(get_db)):
    try:
        _user = await UsersRepo.find_by_username(db, Users, request.parameter["username"])
        
        if not pwd_context.verify(request.parameter.data["password"], _user.password):
            return ResponseSchema(
                code=400, status="Bad Request", message="Invalid password"
            ).dict(exclude_none=True)
        
        token = JWTRepo.generate_token({"sub": _user.username})
        return ResponseSchema(
            code=200, status="OK", message="success login!", 
            result=TokenResponse(access_token=token), token_type="Bearer"
        ).dict(exclude_none=True)
    except Exception as e:
        print(e.args)
        return ResponseSchema(code=500, status="Internal Server Error", message="Internal Server Error")