import logging
import os
from datetime import datetime

def get_logger(name="automation"):
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        logfile = f"logs/{datetime.now().strftime('%Y-%m-%d')}.log"
        handler = logging.FileHandler(logfile)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
