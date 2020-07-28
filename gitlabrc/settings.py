# -*- coding: utf-8 -*-

from os import environ
from typing import Text, Type, Optional

class Config:

  @staticmethod
  def get_env(env: Type[Text], default: Optional[Type[Text]] = None) -> Text:
    return environ.get(env, default)
