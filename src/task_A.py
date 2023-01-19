def ascii_to_hex(ascii_data):
    return ascii_data.encode('utf-8').hex()


def hex_to_ascii(hex_data):
    return bytearray.fromhex(hex_data).decode()


def XOR_hex(text, key):
    return int(text, 16) ^ int(key, 16)


def XOR_text(text, key):
    # implement a way to make text and key same length
    length_diff:int = len(text) - len(key)
    if length_diff > 0: # text is longer than key
        # do some tests to see if this is right
        key = int(length_diff / len(key) + 1) * key + key[:length_diff % len(key)]
    if length_diff < 0: # text is shorter than key
        key = key[0:len(text)]
    return XOR_hex(ascii_to_hex(text), ascii_to_hex(key))


print(XOR_text("paul", "paul"), " -> expect 0 ")
print(XOR_text("pa", "paul"), " -> expect 0 ")
print(XOR_text("papa", "pa"), " -> expect 0 ")

