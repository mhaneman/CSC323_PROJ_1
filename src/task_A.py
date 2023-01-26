import binascii


def ascii_to_hex(ascii_string):
    return ascii_string.encode("ascii").hex()


def hex_to_ascii(hex_string: str):
    try:
        return bytearray.fromhex(hex_string).decode(encoding="utf-8", errors="ignore")
    except Exception:
        return None

def bytes_to_ascii(byte_str: str):
    try:
        return byte_str.decode(encoding="utf-8", errors="ignore")
    except Exception:
        return None



def XOR_bytes(byte_str: str, key: str):
    length_diff: int = len(byte_str) - len(key)
    if length_diff > 0:  # text is longer than key
        key = key * int(length_diff // len(key) + 1) + key[:length_diff % len(key)]
    elif length_diff < 0:  # text is shorter than key
        key = key[0:len(byte_str)]

    return bytes([_a ^ _b for _a, _b in zip(byte_str, key)])

def XOR_hex(hex_str: str, key_str: str) -> str:
    byte_str = bytes.fromhex(hex_str)
    byte_key = bytes.fromhex(key_str)

    return XOR_bytes(byte_str, byte_key)
