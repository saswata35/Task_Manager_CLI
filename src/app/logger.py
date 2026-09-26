import logging

from src.config import LOGGER_FILENAME

logger = logging.getLogger("-------Task Manager CLI--------")
logging.basicConfig(
    format = "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level = logging.INFO,
    filename = LOGGER_FILENAME
)

