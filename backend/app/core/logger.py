import logging
from logging.handlers import RotatingFileHandler

from app.core.config import settings

logger = logging.getLogger(__name__)
if settings.ENVIRONMENT == "development":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
else:
    logging.basicConfig(
        filename="logs/backend.log",
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    handler = RotatingFileHandler("logs/backend.log", maxBytes=100000, backupCount=10)
