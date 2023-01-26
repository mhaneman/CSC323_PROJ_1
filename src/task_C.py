import task_A
from langdetect import detect_langs


def english_prob(text: str, dev_thresh: float) -> float:
    letter_prob = 1 / len(text)
    test_letters = [{'e': 0.13}, {'a', 0.82}, {'t': 0.91}]
    found_letters = [{'e': 0.0}, {'a', 0.0}, {'t', 0.0}]
    
    for n in text:
        for i in found_letters:
            for key, val in i:
                if key == n:
                    val += letter_prob

    print(found_letters)

    return 0.0

def XOR_64(text_64: str, key: str):
    pass

def parse_file(filename: str, key: str):
    with open(filename, "r") as f:
        for line in f:
            h = task_A.XOR_hex(line[:-1], key)
            t = task_A.bytes_to_ascii(h)

            if t is not None and english_prob(t) > 0.8:
                print(t)


if __name__ == "__main__":
    FILENAME = "../docs/Lab0.TaskII.C.txt"
    for i in range(1, 10000):
    parse_file(FILENAME, bytes(i))
