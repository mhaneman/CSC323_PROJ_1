import task_A
from langdetect import detect_langs


# how likely is a string of text english
def english_prob(text) -> float:
    try:
        detected_languages = detect_langs(text)
        for lang in detected_languages:
            if lang.lang == 'en':
                return lang.prob
        return 0.0
    except Exception:
        return 0.0

def key_prob(text):
    num_of_e = text.count('e')
    return num_of_e




def parse_file(filename: str, key: str):
    with open(filename, "r") as f:
        for line in f:
            h = task_A.XOR_hex(line[:-1], key)
            t = task_A.bytes_to_ascii(h)

            if t is not None and key_prob(t) > 4:
                print(t)


if __name__ == "__main__":
    FILENAME = "../docs/Lab0.TaskII.B.txt"
    for i in range(0, 255):
        key = hex(i)[2:]
        if len(key) % 2 != 0:
            key += str(0)

        parse_file(FILENAME, key)
