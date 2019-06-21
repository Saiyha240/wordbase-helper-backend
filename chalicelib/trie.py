import json
import time


class TrieNode(object):

    def __init__(self, char: str) -> None:
        self.char = char
        self.children = {}
        self.word = None

    def __str__(self) -> str:
        return self.char


class TrieBase(TrieNode):

    def __init__(self) -> None:
        super().__init__('*')

        self.populate()

    def __str__(self):
        return self.char

    def populate(self) -> None:
        data = json.loads(open('./chalicelib/data/words_dictionary.json').read())
        start_time = time.time()

        for word in data:
            self.add(word)

        print("--- Initialized Trie in %s seconds ---" % (time.time() - start_time))

    def add(self, word: str) -> None:
        current_node = self

        for char in word:
            if char in current_node.children:
                child = current_node.children[char]
            else:
                child = TrieNode(char)
                current_node.children[char] = child

            current_node = child

        current_node.word = word

    def find_word_node(self, word: str) -> TrieNode:
        top_node = self

        for char in word:
            if char in top_node.children:
                top_node = top_node.children[char]
            else:
                return None

        return top_node

    def is_word_exists(self, word: str) -> bool:
        word = word.lower()
        word_node = self.find_word_node(word)

        if word_node and word_node.word == word:
            return True

        return False
