import config
from db import Base
from pytz import timezone
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    email = Column(String(64), nullable=False)
    phone = Column(String(32), nullable=False)
    
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(128), nullable=False)
    
    create_date = Column(DateTime(timezone(config.TIMEZONE)), default=datetime.now(timezone(config.TIMEZONE)), nullable=False)
    update_date = Column(DateTime(timezone(config.TIMEZONE)), default=datetime.now(timezone(config.TIMEZONE)), nullable=True)
