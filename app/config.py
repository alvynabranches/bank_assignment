import os
import asyncio

KAFKA_TOPIC = "messages"

ANNUAL_INC_COL = "annual_inc"
loop = asyncio.get_event_loop()

DATABASE_URL = os.environ.get("DATABASE_URL", "db")
MYSQL_USER = os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "alvyn")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "transaction_db")
KAFKA_BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "").split(",")
