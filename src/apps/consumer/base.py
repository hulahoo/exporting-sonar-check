import json

from loguru import logger

from src.apps.consumer.abstract import AbstractConsumer
from src.apps.producer.syslog_sender import syslog_sender


class BaseConsumer(AbstractConsumer):

    def start_process(self):
        self.start_consumer()
        self.process_handler_service()

    def process_handler_service(self):
        logger.info("Start process services...")

        for event in tuple(self.consumer.poll(timeout_ms=5000).items()):
            message = json.loads(event.value)
            try:
                syslog_sender(data_to_send=message)
            except Exception as e:
                logger.exception(f"Failed proccess message with error: {e}")
                continue


base_consumer = BaseConsumer()
