import os


def extractwords():
    file_path = os.path.join(os.path.dirname(__file__), "words.txt")

    with open(file_path, "r") as f:
        words = f.read().splitlines()
        f.close()

    words_stripped = list(map(lambda word: word.strip(), words))
    return words_stripped
