# -*- coding: utf-8 -*-

from collections import defaultdict
from typing import List, DefaultDict


class Tree:
    @staticmethod
    def make(information: List[List[str]]) -> DefaultDict[str, "DefaultDict"]:
        tree = lambda: defaultdict(tree)
        dictionary = tree()
        for element in information:
            aux = dictionary
            for item in element:
                aux = aux[item]
        return dictionary

    def make_strs(
        self, dictionary: DefaultDict[str, "DefaultDict"], indent: int = 0,
    ) -> List[str]:
        strings = []
        for key, value in dictionary.items():
            strings.append("  " * indent + str(key))
            strings.extend(self.make_strs(value, indent + 1))
        return strings

    def show(self, dictionary: DefaultDict[str, "DefaultDict"]) -> None:
        print("\n".join(self.make_strs(dictionary)))
