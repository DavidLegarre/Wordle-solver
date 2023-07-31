from dictionary.wordextractor import extractwords
from .guesses import WordTree

message = """
I recommend starting with "salet" as shown in https://www.youtube.com/watch?v=fRed0Xmc2Wg
To input your guesses you must type the 5 letters you've tried,
if the letter is in the correct position it must be follow by a '+' symbol,
and if the letter is correct but not in the correct position it must be followed
by a '-' symbol, otherwise it will guess the letters is not in the word.
When you've inputted all your guesses press enter to start solving.
"""

words = ["", "", "", "", ""]
# Correct letters and position
correct_letters = ["", "", "", "", ""]
# Correct letters but not position
corr_bad_pos = ["", "", "", "", ""]
# Incorrect letters tried
incorrect_letters = set()


def parse_word(word):
    # This function takes the guess provided by the user and interprets it
    # storing it in the correct way to later calculate guesses

    for i, letter in enumerate(word):
        try:
            if word[i + 1] == "+":
                correct_letters[i] = letter
                # If the letter was in a bad position remove it
                if letter in corr_bad_pos:
                    corr_bad_pos[corr_bad_pos.index(letter)] = ""
            if word[i + 1] == "-":
                corr_bad_pos[i] = letter
            else:
                if word[i] not in correct_letters:
                    incorrect_letters.add(letter)
        except Exception:
            if letter == "+" or letter == "-":
                pass
            incorrect_letters.add(letter)


def calculate_predictions(dictionary, wordtree: WordTree):
    # TODO: Implement the predictions using WordTree class
    for letter in incorrect_letters:
        wordtree.delete_word_letter(letter)
    return wordtree.guess


def solver():
    dictionary = extractwords()
    wordtree = WordTree(dictionary)
    wordtree.initialize_tree()

    print(message)
    print("Input the guesses:\n")

    for i in range(4):
        if i == 4:
            print("Least attempt before solving")
        word = input()
        if word == "":
            break
        parse_word(word)
        print(word)
        print(f"Correct letters positions:\n{correct_letters}")
        print(f"Correct letters but wrong positions:\n{corr_bad_pos}")
        print(f"wrong letters:\n {incorrect_letters}")

        calculate_predictions(dictionary, wordtree)
