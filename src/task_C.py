import task_A
import base64


def english_p_value(text: str) -> float:
    letter_prob = 1 / len(text)
    EXPECTED_E_FREQ = 0.13
    e_freq = 0

    for n in text:
        if n == "e" or n == "E":
            e_freq += letter_prob

    return e_freq


def maybe_english(text: str):
    score = 0

    for n in text:
        if ord(n) != 34 and (ord(n) < 97 or ord(n) > 122):
            score -= 0.5
        if n == "e" or n == "E" or n == "a" or n == "A" or  n == "t" or n == "T":
            score += 1.2

    if score >= 3:
        return True
    return False


def XOR_64(text_64: str, key: str):
    text_byte = base64.b64decode(text_64)
    return task_A.XOR_bytes(text_byte, key)


def parse_file(filename: str, key: str):
    with open(filename, "r") as f:
        for line in f:
            h = XOR_64(line[:-1], key)
            t = task_A.bytes_to_ascii(h)

            if t is not None and maybe_english(t):
                print(t)


def generate_key(int_val):
    radix = 256
    vals = []
    dec = int_val
    while True:
        q = dec // radix
        if q == 0:
            vals.append(dec)
            break
        else:
            vals.append(dec % radix)
        dec = q

    vals = list(reversed(vals))

    if vals is None:
        return bytes([0])
    return bytes(vals)


if __name__ == "__main__":
    FILENAME = "../docs/Lab0.TaskII.C.txt"
    for i in range(1, 10000000000000):
        key = generate_key(i)
        parse_file(FILENAME, key)
