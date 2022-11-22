import os
import json
from time import sleep
from logging import getLogger
from kafka import KafkaConsumer

container = os.environ.get("CONTAINER", None) == "true"

if container:
    for i in range(n:=60*3):
        sleep(1)
        print(n-i-1, end="\r")

consumer = KafkaConsumer("messages", bootstrap_servers=["kafka:9093" if container else "localhost:9093"], auto_offset_reset="earliest")
logger = getLogger(__name__)

if __name__ == "__main__":
    try:
        for message in consumer:
            print("Consumer:", type(message.value))
            print("Consumer:", json.loads(message.value))
            logger.info("consumed message successfully!")
    except KeyboardInterrupt:
        consumer.close()
        logger.info("consumer closed!")
        print("consumer closed!")
