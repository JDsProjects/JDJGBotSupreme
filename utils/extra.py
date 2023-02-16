HEX_ALPHABET_MAP = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}


def convert_to_int(hexs: str) -> int:
    v = int(HEX_ALPHABET_MAP.get(hexs[0], hexs[0])) * 16
    v += int(HEX_ALPHABET_MAP.get(hexs[1], hexs[1]))
    return v


def invert(v: int) -> int:
    return 255 - v


def convert_to_hex(v: int):
    d = hex(v)[2:].upper()
    if len(d) == 1:
        d = f"0{d}"
    return d


def invert_sm64_str(text: str):
    e = []
    for i in text.splitlines():
        if not i:
            continue
        addr, hex = i.split(" ")
        fh = hex[:2]
        sh = hex[2:4]
        nhex = convert_to_hex(invert(convert_to_int(fh)))
        if sh != "00":
            nhex += convert_to_hex(invert(convert_to_int(sh)))
        else:
            nhex += f"00"
        e.append(f"{addr} {nhex}")
    return "\n".join(e)


# sm64 inverting methods created by Juuzoq


# (check that it's 13 characters)
# <8> <space> <4>
# repeat?


def color_code_checker(text: str):
    return True


# something else later
