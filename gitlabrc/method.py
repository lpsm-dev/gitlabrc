from enum import Enum
from typing import Text, Type

"""
https://docs.python.org/3/library/enum.html
https://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
"""

class CloneMethod(Enum):
  HTTP = 1
  SSH = 2

  @staticmethod
  def parse(method: Type[Text]) -> Enum:
    return CloneMethod[method.upper()]
