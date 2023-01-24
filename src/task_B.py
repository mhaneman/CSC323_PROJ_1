import task_A
from langdetect import detect_langs


# how likely is a string of text english
def english_prob(text) -> float:
    detected_languages = detect_langs(text)
    for lang in detected_languages:
        if lang.lang == 'en':
            lang.prob


def parse_file(filename, key):
    with open(filename, "r") as f:
        for line in f:
            h = task_A.XOR_hex(line, key)
            t = task_A.hex_to_ascii(h)
            if english_prob(t) > 0.9:
                print(t)


if __name__ == "__main__":
    FILENAME = "../docs/Lab0.TaskII.B.txt"
    for i in range(0, 127):
        parse_file(FILENAME, int(i, 16))
