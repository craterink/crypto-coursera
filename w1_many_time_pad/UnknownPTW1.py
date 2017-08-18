from UnknownPTLetterW1 import UnknownPTLetterW1
import math

class UnknownPTW1:

    _unknown_ltrs = []

    def __init__(self, cipher):
        ascii_length = int(math.ceil(math.log(cipher + 1, 16)))
        self._unknown_ltrs = [UnknownPTLetterW1() for i in range(ascii_length)]

    def __getitem__(self, item):
        return self._unknown_ltrs[item]
