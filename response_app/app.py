import os
import json
import pandas as pd
from time import sleep
from fastapi import FastAPI
from logging import getLogger
from kafka import KafkaConsumer

from config import ANNUAL_INC_COL

container = os.environ.get("CONTAINER", None) == "true"

if container:
    for i in range(n:=60*3):
        sleep(1)
        print(n-i-1, end="\r")

consumer = KafkaConsumer("messages", bootstrap_servers=["kafka:9093" if container else "localhost:9093"], auto_offset_reset="earliest")
logger = getLogger(__name__)
df = pd.DataFrame()

if __name__ == "__main__":
    try:
        for message in consumer:
            _temp = pd.DataFrame(message.value)
            df = pd.concat([df, _temp], axis=0)
    except KeyboardInterrupt:
        consumer.close()
        logger.info("consumer closed!")
        print("consumer closed!")
