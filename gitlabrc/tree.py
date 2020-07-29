from collections import defaultdict
from typing import Type, List, DefaultDict, Text, NoReturn, Optional

class Tree:

  @staticmethod
  def make(information: Type[List[Text]]) -> DefaultDict: 
    tree = lambda: defaultdict(tree)
    dictionary = tree()
    for element in information:
      aux = dictionary
      for item in element:
        aux = aux[item]
    return dictionary

  def make_strs(self, 
    dictionary: DefaultDict, 
    indent: Optional[Type[int]] = 0
  )  -> List:
    strings = []
    for key, value in dictionary.items():
      strings.append("  " * indent + str(key))
      strings.extend(self.make_strs(value, indent + 1))
    return strings

  def show(self, dictionary: DefaultDict) -> NoReturn:
    print("\n".join(self.make_strs(dictionary)))
