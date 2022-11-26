import os
import config
from sqlalchemy import create_engine, MetaData

conn_url = f"mysql+pymysql://{config.MYSQL_USER}{'' if len(config.MYSQL_PASSWORD) == 0 else ':'}{config.MYSQL_PASSWORD}@{config.DATABASE_URL}:3306/{config.MYSQL_DATABASE}"
print("Connection URL:", conn_url)
engine = create_engine(conn_url)

meta = MetaData()
conn = engine.connect()
