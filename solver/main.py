from dictionary.wordextractor import extractwords
from .guesses import WordTree

message = """
I recommend starting with "salet" as shown in 
https://www.youtube.com/watch?v=fRed0Xmc2Wg
"""

words = ["", "", "", "", ""]
# Correct letters and position
correct_letters = ["", "", "", "", ""]
# Correct letters but not position
corr_bad_pos = ["", "", "", "", ""]
# Incorrect letters tried
incorrect_letters = set()


def parse_word(word, hits, close):
    # This function takes the guess provided by the user and interprets it
    # storing it in the correct way to later calculate guesses

    for pos in hits:
        pos = pos - 1
        correct_letters[pos] = word[pos]

    for pos in [*close]:
        pos = pos - 1
        corr_bad_pos[pos] = word[pos]

    for char in word:
        if char not in correct_letters and char not in corr_bad_pos:
            incorrect_letters.add(char)

    return word


def calculate_predictions(wordtree: WordTree):
    # TODO: Make word prediction smarter
    # Now trying a frequentist analysis
    for letter in incorrect_letters:
        print(letter)
        wordtree.delete_word_letter(letter)

    for i, letter in enumerate(correct_letters):
        if letter:
            guess_set = wordtree.words_with_letter_at_position(letter, i + 1)
            wordtree.update_guess(guess_set)

    for i, letter in enumerate(corr_bad_pos):
        if letter:
            guess_set = wordtree.words_with_letter_not_at_position(
                letter, i + 1)
            wordtree.update_guess(guess_set)

    return wordtree.guess


def solver():
    dictionary = extractwords()
    wordtree = WordTree(dictionary)
    wordtree.initialize_tree()

    print(message)
    print("Input the guesses:\n")

    for i in range(1, 6):
        if i == 4:
            print("Least attempt before solving")
        word = input(f"Guess {i}:\n")
        hits = list(map(int, input("Green positions:\n").split()))
        close = list(map(int, input("Yellow positions:\n").split()))
        if word == "":
            break
        parse_word(word, hits, close)
        # print(word)
        # print(f"Correct letters positions:\n{correct_letters}")
        # print(f"Correct letters but wrong positions:\n{corr_bad_pos}")
        print(f"Wrong letters:\n {incorrect_letters}")
        # print(f"Placed letters:\n {letters_placed}")

        calculate_predictions(wordtree)

        print(f"Try {wordtree.get_guess()} ")
        # print(f"New Guesses:{sorted(list(wordtree.guess))}")
