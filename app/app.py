import json
import config
import asyncio
import pandas as pd
from db import conn, engine
from schema import RejectedData
from fastapi import FastAPI
from models import transactions, transactions_information
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.background import BackgroundTasks
from kafka import KafkaProducer, KafkaConsumer
from logging import getLogger

app = FastAPI()
logger = getLogger(__name__)

def backgroundtask(transaction_id: int, ip: str, port: str, endpoint: str):
    conn.execute(transactions_information.insert().values(
        transaction_id=transaction_id,
        ip=ip,
        port=port,
        endpoint=endpoint
    ))

@app.get("/")
async def index(request: Request, background: BackgroundTasks):
    client_host, client_port = str(request.client.host), str(request.client.port)
    # background.add_task(backgroundtask, 0, client_host, client_port, "transaction")
    return JSONResponse({"status": "success"}, 200)

async def consume():
    consumer = KafkaConsumer(
        config.KAFKA_TOPIC,
        # loop=config.loop, # Only for AIOKafkaConsumer
        bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS,
        auto_offset_reset="earliest"
    )
    df = pd.DataFrame()
    try:
        # await consumer.start() # Only for AIOKafkaConsumer
        for msg in consumer:
            df = pd.concat([df, pd.DataFrame(msg)], axis=0, ignore_index=True)
            MA50 = df[config.TARGET_COL].rolling(50).mean().tolist()[-1]
            EMA50 = df[config.TARGET_COL].ewm(span=50, adjust=False).mean().tolist()[-1]
            MA100 = df[config.TARGET_COL].rolling(100).mean().tolist()[-1]
            conn.execute(transactions.insert().values(
                **msg,
                **{
                    f"{config.TARGET_COL}_MA50": MA50,
                    f"{config.TARGET_COL}_EMA50": EMA50,
                    f"{config.TARGET_COL}_MA100": MA100
                }
            ))
    except Exception as e:
        print(e)
        logger.error(e)
    # finally:
    #     await consumer.stop() # Only for AIOKafkaConsumer
	

def back(new_data: dict):
    all_transactions = conn.execute(transactions)
    df = pd.read_sql("select * from transactions;", con=engine)
    df = pd.DataFrame(all_transactions, columns=["id", "amount_requested", "application_date", "loan_title", "risk_score", "debt_to_income_ratio", "zip_code", "state", "employment_length", "policy_code", f"{config.TARGET_COL}_MA50", f"{config.TARGET_COL}_EMA50", f"{config.TARGET_COL}_MA100"])
    MA50 = df[config.TARGET_COL].rolling(50).mean().tolist()[-1]
    EMA50 = df[config.TARGET_COL].ewm(span=50, adjust=False).mean().tolist()[-1]
    MA100 = df[config.TARGET_COL].rolling(100).mean().tolist()[-1]
    conn.execute(transactions.insert().values(
        **new_data, 
        **{
            f"{config.TARGET_COL}_MA50": MA50, 
            f"{config.TARGET_COL}_EMA50": EMA50, 
            f"{config.TARGET_COL}_MA100": MA100
        }
    ))
    
    
@app.post("/transaction")
async def transaction(message: RejectedData, request: Request, background: BackgroundTasks):
    client_host, client_port = str(request.client.host), str(request.client.port)
    producer = KafkaProducer(
        # loop=config.loop, # Only for AIOKafkaProducer
        bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS
    )
    try:
        # await producer.start() # Only for AIOKafkaProducer
        json_value = json.dumps(message.__dict__).encode("utf-8")
        producer.send(topic=config.KAFKA_TOPIC, value=json_value)
        conn.execute(transactions.insert(message.__dict__))
    except Exception as e:
        print(e)
        logger.error(e)
    # finally:
    #     await producer.stop() # Only for AIOKafkaProducer
    # background.add_task(backgroundtask, message.id, client_host, client_port, "transaction")
    background.add_task(consume)
    back(message.__dict__)
    return JSONResponse({"status": "created"}, 201)

# asyncio.create_task(consume()) # Only for aiokafka module
