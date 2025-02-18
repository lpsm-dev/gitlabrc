# -*- coding: utf-8 -*-

from os import environ
from typing import Optional


class Config:
    @staticmethod
    def get_env(env: str, default: Optional[str] = None) -> Optional[str]:
        return environ.get(env, default)
