def calculate_letter_freq(word):
    frequency = {}
    for char in word:
        frequency[char] = frequency.get(char, 0) + 1

    return frequency


class TreeNode:
    def __init__(self) -> None:
        self.children = {}
        self.words = set[str]()
        self.is_end_of_word = False

    def delete_letter(self, letter):
        if letter in self.children:
            del self.children[letter]

    def __str__(self):
        arr = []
        for word in self.words:
            arr.append(word)
        return str(arr)

    def __getitem__(self, item):
        item = str(item)
        return self.children[item]

    def __setitem__(self, key, newvalue):
        self.children[key] = newvalue

    def __contains__(self, item):
        return item in self.children.keys()


class WordTree:
    def __init__(self, dictionary) -> None:
        self.dictionary = dictionary
        self.root = TreeNode()
        self.guess = set[str]()

        for i in range(1, 6):
            self.root.children[str(i)] = TreeNode()

        print(self.root.children.keys())

    def insert(self, word):
        assert len(word) == 5, "Only words of length 5"
        for i, char in enumerate(word):
            i = str(i + 1)
            position = self.root.children[i]
            if char not in position:
                position.children[char] = TreeNode()
            position.children[char].words.add(word)

    def initialize_tree(self):
        for word in self.dictionary:
            self.insert(word)

    def intersection(self, a, b):
        if a and b:
            return a & b
        else:
            return a if a else b

    def words_with_letter_at_position(self, letter, position):
        node = self.root
        position = str(position)
        node_pos = node[position]
        if letter in node_pos:
            return node_pos[letter].words

    def words_with_letter_not_at_position(self, letter, position):
        node = self.root
        position = str(position)
        words = set()
        for pos in range(1, 6):
            pos = str(pos)
            if pos == position:
                continue
            if not words:
                words = node[pos][letter].words.copy()
            words = words | node[pos][letter].words
        return words

    def delete_word_letter(self, letter):
        node = self.root
        for pos in range(1, 6):
            if letter in node[pos]:
                self.update_guess(node[pos][letter].words, "d")
                node[pos][letter].delete_letter(letter)

    def delete_word_letter_at_position(self, letter, position):
        node = self.root
        position = str(position)
        print(position)
        if letter in node[position]:
            self.update_guess(node[position][letter].words, "d")
            # print(f"Deleting letter {letter} at position {position}")
            node[position][letter] = TreeNode()
        print(node[position][letter])

    def update_guess(self, guess_update, mode="U"):
        if mode == "U":
            self.guess = self.intersection(self.guess, guess_update)
        elif mode == "d":
            self.guess -= guess_update

    def letter_freq(self):
        frequency = {}
        for word in self.guess:
            for letter in word:
                frequency[letter] = frequency.get(letter, 0) + 1

        return frequency

    def get_guess(self):
        highest_sum = 0
        max_word = None
        frequency = self.letter_freq()
        # Get the top 10 most frequent letters for now
        top_freq = sorted(frequency, key=frequency.get, reverse=False)[:10]

        for word in self.guess:
            word_freq = calculate_letter_freq(word)
            freq_sum = sum(word_freq.get(letter, 0) for letter in top_freq)

            if freq_sum > highest_sum:
                highest_sum = freq_sum
                max_word = word

        return max_word
