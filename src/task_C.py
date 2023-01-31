import task_A
import base64
import random


def maybe_english(text: str):
    score = 0

    if len(text) < 40:
        return False

    for n in text:
        if ord(n) > 122:
            return False
        if n == "e" or n == "E" or n == "a" or n == "A" or  n == "t" or n == "T":
            score += 1.5

    if score >= 0:
        return True
    return False


def XOR_64(text_64: str, key: str):
    text_byte = base64.b64decode(text_64)
    return task_A.XOR_bytes(text_byte, key)


def parse_file_res(filename: str, key: str):
    with open(filename, 'r') as file:
        data = file.read()
        h = XOR_64(data, key)
        if has_res(h):
            print("key length: ", len(key))


def random_n_key(length: int):
    vals = []
    for i in range(0, length):
        vals.append(random.randrange(256))
    return bytes(vals)


def has_res(text: str) -> bool:
    byte_dict = {}
    for t in text:
        if t in byte_dict:
            byte_dict[t] += 1
        else:
            byte_dict[t] = 1

    for key, val in byte_dict.items():
        if val >= 20:
            return True
    return False


def parse_file_spaced(filename, key):
    with open(filename, 'r') as file:
        data = file.read()
        data_byte = base64.b64decode(data)

        data_byte = data_byte[2::5]

        b = task_A.XOR_bytes(data_byte, key)
        text = task_A.bytes_to_ascii(b)


        if text is not None and maybe_english(text):
            print("KEY --> ", task_A.bytes_to_ascii(key), " --> ", key)
            print(text)

def parse_file(filename, key):
    with open(filename, 'r') as file:
        data = file.read()
        h = XOR_64(data, key)
        print(h)

# key of length 5
# 0 --> a
# 1 --> y 
# 2 --> b'\xb5'
# 3 --> b'\xe7' 
# 4 --> b'Z' 
if __name__ == "__main__":
    FILENAME = "../docs/Lab0.TaskII.C.txt"
    #for i in range(1, 20):
    #    key = random_n_key(5)
    #    parse_file_res(FILENAME, key)

    #for i in range(0, 256):
    #    key = bytes([i])
    #    parse_file_spaced(FILENAME, key)

    b = bytes([97, 121, 181, 231, 90])
    parse_file(FILENAME, b)
