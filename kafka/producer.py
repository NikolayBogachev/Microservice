from aiokafka import AIOKafkaProducer
import json


KAFKA_BROKER = "kafka:9092"
TOPIC_NAME = "applications"


async def get_producer():
    producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BROKER)
    await producer.start()
    return producer


async def publish_to_kafka(application):
    producer = await get_producer()
    try:
        message = {
            "id": application.id,
            "user_name": application.user_name,
            "description": application.description,
            "created_at": str(application.created_at),
        }
        await producer.send_and_wait(TOPIC_NAME, json.dumps(message).encode("utf-8"))
    finally:
        await producer.stop()
