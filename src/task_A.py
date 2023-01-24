def ascii_to_hex(ascii_data):
    return ascii_data.encode('utf-8').hex()


def hex_to_ascii(hex_data):
    return bytearray.fromhex(hex_data).decode()


def XOR_hex(hex_str: str, key: str):
    length_diff: int = len(hex_str) - len(key)
    if length_diff > 0:  # text is longer than key
        key = int(length_diff / len(key) + 1) * key + key[:length_diff % len(key)]
    if length_diff < 0:  # text is shorter than key
        key = key[0:len(hex_str)]
    return int(hex_str, 16) ^ int(key, 16)


def XOR_text(text: str, key: str):
    return XOR_hex(ascii_to_hex(text), ascii_to_hex(key))


print(XOR_text("paul", "paul"), " -> expect 0 ")
print(XOR_text("pa", "paul"), " -> expect 0 ")
print(XOR_text("papa", "pa"), " -> expect 0 ")
