from convert import hexstr2dec, dec2hexstr


class Hex:

    hex_str = None

    def __init__(self, hex_str):
        self._hex_str = hex_str

    def __xor__(self, other):
        (dec1, dec2) = (hexstr2dec(self.hex_str), hexstr2dec(other.hex_str))
        xor = dec1 ^ dec2
        return Hex(dec2hexstr(xor))