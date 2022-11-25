import os
from sqlalchemy import create_engine, MetaData

DATABASE_URL = os.environ.get("DATABASE_URL", "db")
MYSQL_USER = os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "transaction_db")

engine = create_engine(
    f"mysql+pymysql://{MYSQL_USER}{':' if len(MYSQL_PASSWORD) == 0 else ''}{MYSQL_PASSWORD}@{DATABASE_URL}:3306/{MYSQL_DATABASE}"
)
meta = MetaData()
conn = engine.connect()
