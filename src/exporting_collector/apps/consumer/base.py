import sys
import json
import traceback

from exporting_collector.config.log_conf import logger
from exporting_collector.apps.worker.handler import syslog_sender
from exporting_collector.apps.consumer.abstract import AbstractConsumer


class BaseConsumer(AbstractConsumer):

    def start_process(self):
        self.start_consumer()
        self.process_handler_service()

    def process_handler_service(self):
        logger.info("Start process services...")  # noqa

        for message in self.consumer.poll(timeout_ms=5000):
            event = json.loads(message.value)
            try:
                logger.info(f'Incoming events fromm is: {message.topic}')

                syslog_sender(message=event)

            except Exception as e:
                exc_info = sys.exc_info()
                traceback.print_exception(*exc_info)
                logger.error(f"FAILED proccess message from topic: {message.topic}")
                logger.error(f"ERROR traceback: {e}")
                continue
