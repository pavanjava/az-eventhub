import asyncio
import logging
import random
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

logger = logging.getLogger("azure.eventhub")
logging.basicConfig(level=logging.INFO)


async def produce():
    producer = EventHubProducerClient.from_connection_string(
        conn_str='<YOUR EVENTHUB CONNECTION STRING>',
        eventhub_name='<YOUR EVENTHUB NAME>')
    async with producer:
        while True:
            temperature = random.randint(15, 45)
            await producer.send_event(EventData(f'temperature: ${temperature}'))


loop = asyncio.get_event_loop()
loop.run_until_complete(produce())
