from dictionary.wordextractor import extractwords
from .guesses import WordTree


def test():
    dictionary = extractwords()
    print(dictionary[:10])
    guesses = WordTree(dictionary)
    guesses.initialize_tree()

    # guesses.print_children()

    print(guesses.words_with_letter_at_position("a", "1"))
