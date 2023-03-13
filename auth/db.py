import config
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

CONN_URL = f"postgresql://{config.POSTGRES_USER}{'' if len(config.POSTGRES_PASSWORD) == 0 else ':'}{config.POSTGRES_PASSWORD}@{config.DATABASE_URL}:{config.DATABASE_PORT}/{config.POSTGRES_DATABASE}"
engine = create_engine(CONN_URL)
conn = engine.connect()
meta = MetaData()
local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base(engine, meta)

def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()
    