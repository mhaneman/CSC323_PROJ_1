import operator 


def parse_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
        return data


def friedman_test(text):
    k_p = 0.067
    k_r = 0.0385
    k_0 = 0.04194
    letter_dict = {}

    for t in text:
        if t in letter_dict:
            letter_dict[t] += 1
        else:
            letter_dict[t] = 1

    for i in letter_dict.values():
        freq = i / len(text)
        k_0 += freq * (freq - 1)

    k_0 /= len(text) * (len(text) - 1)
    return (k_p - k_r) / (k_0 - k_r)


def viggy(text, key):
    length_diff = len(text) - len(key)
    key = key * int(length_diff // len(key) + 1) + key[:length_diff % len(key)]

    result = ""
    for i in range(len(text)):
        result += shift_letter(text[i], key[i])
    return result


def shift_letter(letter, key):
    return chr((ord(letter) - ord(key)) % 26 + 65)


def maybe_english(text):
    letter_freq = { 
                   'A': 0.082,
                   'B': 0.015,
                   'C': 0.028,
                   'D': 0.043,
                   'E': 0.13,
                   'F': 0.022,
                   'G': 0.02,
                   'H': 0.061,
                   'I': 0.07,
                   'J': 0.0015,
                   'K': 0.0077,
                   'L': 0.04,
                   'M': 0.024,
                   'N': 0.067,
                   'O': 0.075,
                   'P': 0.019,
                   'Q': 0.00095,
                   'R': 0.06,
                   'S': 0.063,
                   'T': 0.09,
                   'U': 0.028,
                   'V': 0.0098,
                   'W': 0.024,
                   'X': 0.0015,
                   'Y': 0.02,
                   'Z': 0.00074}
    byte_dict = {}
    for t in text:
        if t in byte_dict:
            byte_dict[t] += 1
        else:
            byte_dict[t] = 1

    chi = 0
    for letter, expect in letter_freq.items():
        obs = 0
        if letter in byte_dict:
            obs = byte_dict[letter] / len(text)
        else:
            obs = 0
        chi += ((obs - expect) ** 2) / expect
    return chi


def spaced_caesar(text, start, length):
    text = text[start::length]
    prob_letters = {}
    for i in range(65, 91):
        t = viggy(text, chr(i))
        prob_letters[chr(i)] = maybe_english(t)

    prob_letters = dict(sorted(prob_letters.items(), key=operator.itemgetter(1)))
    print("potential letters --> ", prob_letters.keys())
    print("\n\n")


# length is probably 4, 7, 8, 14, 16
if __name__ == "__main__":
    FILENAME = "../docs/Lab0.TaskII.D.txt"
    message = parse_file(FILENAME)

    length = 14
    for i in range(length):
        spaced_caesar(message, i, length)

    print (viggy(message, "MOMONEYMOPROBS"))
