import asyncio

KAFKA_BOOTSTRAP_SERVERS = [ "kafka:9093" ]
KAFKA_TOPIC = "messages"

ANNUAL_INC_COL = "annual_inc"
loop = asyncio.get_event_loop()
