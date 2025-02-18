# -*- coding: utf-8 -*-

from enum import Enum
from typing import Text
from dataclasses import dataclass, field
from gitlab.client import Gitlab
import gitlab.exceptions as exceptions
from loguru import logger


class CloneMethod(Enum):
    HTTP = 1
    SSH = 2

    @staticmethod
    def parse(method: str) -> "CloneMethod":
        try:
            return CloneMethod[method.upper()]
        except KeyError:
            from argparse import ArgumentTypeError

            raise ArgumentTypeError(f"Invalid clone method: {method}")


@dataclass
class GitLabBase:
    url: Text = field(default="https://gitlab.com")
    token: Text = field(repr=False, default_factory=Text)

    @property
    def client(self) -> Gitlab:
        try:
            instance = Gitlab(self.url, private_token=self.token)
            instance.auth()
        except exceptions.GitlabAuthenticationError as error:
            logger.error(f"GitLab authentication error - {error}")
            exit()
        else:
            return instance
