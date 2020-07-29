# -*- coding: utf-8 -*-

import logging
import coloredlogs
from typing import NoReturn, Text
from pythonjsonlogger import jsonlogger
from abc import ABCMeta, abstractmethod
from typing import NoReturn, Text, List

class StrategyHandler(metaclass=ABCMeta):

  @abstractmethod
  def handler(self, *args, **kwargs) -> NoReturn:
    pass

class ContextHandler:

  def __init__(self, strategy: StrategyHandler) -> NoReturn:
    self._strategy = strategy

  @property
  def strategy(self) -> StrategyHandler:
    return self._strategy

  def get_handler(self, *args, **kwargs) -> NoReturn:
    return self._strategy.handler(*args, **kwargs)

class BaseFileHandler(StrategyHandler):

  @staticmethod
  def handler(*args, **kwargs) -> logging.FileHandler:
    file_handler = logging.FileHandler(filename=kwargs["log_file"])
    file_handler.setLevel(kwargs["log_level"])
    file_handler.setFormatter(jsonlogger.JsonFormatter(kwargs["formatter"]))
    return file_handler

class BaseStreamHandler(StrategyHandler):

  @staticmethod
  def handler(*args, **kwargs) -> logging.StreamHandler:
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(kwargs["log_level"])
    stream_handler.setFormatter(jsonlogger.JsonFormatter(kwargs["formatter"]))
    return stream_handler

class SingletonLogger(type):

  _instances = {}

  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      cls._instances[cls] = super(SingletonLogger, cls).__call__(*args, **kwargs)
    return cls._instances[cls]

class Log(metaclass=SingletonLogger):

  def __init__(self, log_path: Text, log_file: Text, log_level: Text, logger_name: Text) -> NoReturn:

    self._log_path = log_path
    self._log_file = log_file
    self._log_level = log_level if log_level in ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"] else None
    self._logger_name = logger_name
    self.formatter = "%(levelname)s - %(asctime)s - %(message)s - %(funcName)s"
    self._logger = logging.getLogger(self.logger_name)
    self._logger.setLevel(self.log_level)
    self._base_configuration_log_colored()
    self._logger.addHandler(ContextHandler(BaseFileHandler()).get_handler(log_file=self.log_file, log_level=self.log_level, formatter=self.formatter))

  def _base_configuration_log_colored(self) -> coloredlogs.install:
    coloredlogs.install(level=self._log_level,
                        logger=self.logger,
                        fmt=self.formatter,
                        milliseconds=True)

  @property
  def log_path(self) -> Text:
    return self._log_path

  @property
  def log_file(self) -> Text:
    return self._log_file

  @property
  def log_level(self) -> Text:
    return self._log_level

  @property
  def logger_name(self) -> Text:
    return self._logger_name

  @property
  def logger(self) -> Text:
    return self._logger
