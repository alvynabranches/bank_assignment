from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root@db:3306/transaction_db")
meta = MetaData()
conn = engine.connect()
