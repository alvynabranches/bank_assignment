import os
from sqlalchemy import create_engine, MetaData

DATABASE_URL = os.environ.get("DATABASE_URL", "db")
DATABASE_URL = "34.125.24.176"
MYSQL_USER = os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "alvyn")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "transaction_db")

conn_url = f"mysql+pymysql://{MYSQL_USER}{'' if len(MYSQL_PASSWORD) == 0 else ':'}{MYSQL_PASSWORD}@{DATABASE_URL}:3306/{MYSQL_DATABASE}"
print("Connection URL:", conn_url)
engine = create_engine(conn_url)

meta = MetaData()
conn = engine.connect()
