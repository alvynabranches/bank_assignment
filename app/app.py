import json
import config
import asyncio
import pandas as pd
from db import conn
from schema import Data
from fastapi import FastAPI
from models import transactions, transactions_information
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.background import BackgroundTasks
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer

app = FastAPI()

def backgroundtask(transaction_id: int, ip: str, port: str):
    conn.execute(transactions_information.insert().values(
        transaction_id=transaction_id,
        ip=ip,
        port=port
    ))

@app.get("/")
async def index():
    return JSONResponse({"status": "success"}, 200)

@app.post("/transaction")
async def transaction(message: Data, request: Request, background: BackgroundTasks):
    client_host, client_port = str(request.client.host), str(request.client.port)
    producer = AIOKafkaProducer(loop=config.loop, bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS)
    try:
        await producer.start()
        json_value = json.dumps(message.__dict__).encode("utf-8")
        response = await producer.send_and_wait(topic=config.KAFKA_TOPIC, value=json_value)
        conn.execute(transactions.insert(json_value.__dict__))
    finally:
        await producer.stop()
    background.add_task(backgroundtask, message.id, client_host, client_port)
    return JSONResponse({"response": response}, 201)

async def consume():
    consumer = AIOKafkaConsumer(config.KAFKA_TOPIC, loop=config.loop, bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS, auto_offset_reset="latest")
    df = pd.DataFrame()
    try:
        await consumer.start()
        async for msg in consumer:
            df = pd.concat([df, pd.DataFrame(await msg)], axis=0, ignore_index=True)
            MA50 = df[config.ANNUAL_INC_COL].ewm(span=50, adjust=False).mean().tolist()[-1]
            MA100 = df[config.ANNUAL_INC_COL].rolling(100).mean().tolist()[-1]
            conn.execute(transactions.insert().values(
                **msg, 
                **{f"{config.ANNUAL_INC_COL}_MA50": MA50, f"{config.ANNUAL_INC_COL}_MA100": MA100}
            ))
    finally:
        await consumer.stop()

asyncio.create_task(consume())
