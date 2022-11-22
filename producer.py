import os
import json
import random
import string
from time import sleep
from logging import getLogger
from pytz import timezone as tz
from kafka import KafkaProducer
from datetime import datetime as dt

def generate_message(sleep_time: int | float, ids: list | tuple = list(range(1, 101))) -> dict:
    sender_id = random.choice(ids)
    
    ids_copy = ids.copy()
    ids_copy.remove(sender_id)
    
    recipient_id = random.choice(ids_copy)
    
    message = ''.join(random.choice(string.ascii_letters) for _ in range(32))
    
    return dict(
        timestamp=str(dt.now(tz("Asia/Kolkata"))), 
        sender_id=sender_id, 
        recipient_id=recipient_id, 
        message=message, 
        sleep_time=sleep_time, 
    )

def serializer(message: str):
    return json.dumps(message).encode("utf-8")

container = os.environ.get("CONTAINER", None) == "true"

if container:
    for i in range(n:=60*3):
        sleep(1)
        print(n-i+1, end="\r")

producer = KafkaProducer(bootstrap_servers=["kafka:9093" if container else "localhost:9093"], value_serializer=serializer)
logger = getLogger(__name__)

if __name__ == "__main__":
    try:
        while True:
            st = random.random() * random.randint(1, 5)
            message = generate_message(st)
            producer.send("messages", message)
            print("Producer:", message)
            logger.debug(message)
            sleep(st)
            logger.info("generated message successfully!")
    except KeyboardInterrupt:
        producer.close()
        logger.info("producer closed!")
        print("producer closed!")
