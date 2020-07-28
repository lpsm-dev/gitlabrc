# -*- coding: utf-8 -*-

from os import environ
from typing import Text, Type, Optional

# https://docs.python.org/3/library/typing.html

class Config:

  @staticmethod
  def get_env(env: Type[Text], default: Optional[Type[Text]] = None) -> Text:
    return environ.get(env, default)
      