from dictionary.wordextractor import extractwords

message = """
To input your guesses you must type the 5 letters you've tried,
if the letter is in the correct position it must be follow by a '+' symbol,
and if the letter is correct but not in the correct position it must be followed
by a '-' symbol, otherwise it will guess the letters is not in the word.
When you've inputted all your guesses press enter to start solving.
"""

words = ["", "", "", "", ""]
correct_letters = ["", "", "", "", ""]
correct_positions = []
incorrect_letters = []


def parse_word(word):
    for i, letter in enumerate(word):
        try:
            if word[i + 1] == "+":
                correct_letters[i] = letter
            if word[i + 1] == "-":
                correct_positions.append(letter)
            else:
                incorrect_letters.append(letter)
        except Exception:
            pass


def solver():
    dictionary = extractwords()
    print(message)
    print("Input the guesses:\n")
    for _ in range(5):
        word = input().strip()
        if word == "\n":
            break
        print(word)
        words.append(word)
