# -*- coding: utf-8 -*-

from loguru import logger
import sys

def setup_logging(log_level="INFO"):
    logger.remove()
    logger.add(sys.stdout, format="{time} {level} {message}", level=log_level)
    logger.add("file.log", rotation="1 week", retention="1 month", level=log_level)
