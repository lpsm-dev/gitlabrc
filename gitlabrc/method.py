from enum import Enum
from typing import Text, Type

class CloneMethod(Enum):
  HTTP, SSH = 1, 2

  @staticmethod
  def parse(method: Type[Text]) -> Enum:
    return CloneMethod[method.upper()]
