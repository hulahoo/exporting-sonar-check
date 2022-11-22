from loguru import logger

from src.config.log_conf import configure
from src.apps.consumer.base import base_consumer

# remove loggers if exists
logger.remove()
# add logger message format
logger.configure(**configure)


if __name__ == "__main__":
    base_consumer.start_process()
