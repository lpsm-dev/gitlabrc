from collections import defaultdict
from typing import Type, List, DefaultDict, Text, NoReturn, Optional

class Tree:

  def make_tree(self, information: Type[List[Text]]) -> DefaultDict: 
    tree = lambda: defaultdict(tree)
    dictionary = tree()
    for x in information:
      curr = dictionary
      for item in x:
        curr = curr[item]
    return dictionary

  def make_strs(self, 
    dictionary: DefaultDict, 
    indent: Optional[Type[int]] = 0
  )  -> List:
    strs = []
    for k, v in dictionary.items():
      strs.append(" " * indent + str(k))
      strs.extend(self.make_strs(v, indent+1))
    return strs

  def print_tree(self, dictionary: DefaultDict) -> NoReturn:
    print("\n".join(self.make_strs(dictionary)))
