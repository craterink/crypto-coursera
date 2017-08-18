
def basenstr2dec(str, base):
    return int(str, base=base)

def hexstr2dec(hex_str):
    return basenstr2dec(hex_str, 16)

def dec2hexstr(dec):
    return hex(dec)[2:] # don't return "0x" portion of converted hex

def hex2ascii(hex):
    # TODO
    pass