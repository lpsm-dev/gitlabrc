# -*- coding: utf-8 -*-

from loguru import logger
import sys

def setup_logging(log_level="INFO"):
    logger.remove()
    logger.add(sys.stdout, format="{time} {level} {message}", level=log_level)
