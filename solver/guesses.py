class TreeNode:
    def __init__(self) -> None:
        self.children = {}
        self.words = set[str]()
        self.is_end_of_word = False

    def __str__(self):
        arr = []
        for word in self.words:
            arr.append(word)
        return str(arr)

    def __getitem__(self, item):
        return self.children[item]

    def __contains__(self, item):
        return item in self.children.keys()


class WordTree:
    def __init__(self, dictionary) -> None:
        self.dictionary = dictionary
        self.root = TreeNode()
        self.guess = set[str]()
        # Create a node for all words containing X letter in first position
        self.root.children["1"] = TreeNode()
        # Create a node for all words containing X letter in second position
        self.root.children["2"] = TreeNode()
        # Create a node for all words containing X letter in third position
        self.root.children["3"] = TreeNode()
        # Create a node for all words containing X letter in fourth position
        self.root.children["4"] = TreeNode()
        # Create a node for all words containing X letter in fifth position
        self.root.children["5"] = TreeNode()

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

    def words_with_letter_at_position(self, letter, position):
        node = self.root
        position = str(position)
        node_pos = node.children[position]
        if letter in node_pos:
            return node_pos[letter].words

    def delete_word_letter(self, letter):
        node = self.root
        for pos in node:
            if letter in pos:
                pos[letter] = TreeNode
