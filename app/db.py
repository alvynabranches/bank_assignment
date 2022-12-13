import os
import config
from sqlalchemy import create_engine, MetaData

conn_url = f"mysql+pymysql://{config.MYSQL_USER}{'' if len(config.MYSQL_PASSWORD) == 0 else ':'}{config.MYSQL_PASSWORD}@{config.DATABASE_URL}:3306/{config.MYSQL_DATABASE}"
engine = create_engine(conn_url, pool_size=20, max_overflow=20)

meta = MetaData()
conn = engine.connect()
meta.bind = engine
