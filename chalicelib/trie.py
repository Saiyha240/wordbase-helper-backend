import json
import time


class TrieNode(object):

    def __init__(self, char: str) -> None:
        self.char = char
        self.children = []
        self.word = None

    def add_child(self, child: 'TrieNode') -> None:
        self.children.append(child)

    def get_child(self, char: [str, 'TrieNode']) -> 'TrieNode':
        try:
            return self.children[self.children.index(char)]
        except ValueError:
            return None

    def set_word(self, word: str) -> None:
        self.word = word

    def has_word(self) -> bool:
        return self.word is not None

    def __str__(self) -> str:
        return self.char

    def __eq__(self, o: object) -> bool:
        if isinstance(o, self.__class__):
            return self.char == o.char
        elif isinstance(o, str):
            return self.char == o

        return super().__eq__(o)

    def __ne__(self, o: object) -> bool:
        if isinstance(o, self.__class__):
            return self.char != o.char
        elif isinstance(o, str):
            return self.char != o

        return super().__ne__(o)


class TrieBase(TrieNode):

    def __init__(self) -> None:
        super().__init__('*')

        start_time = time.time()

        data = json.loads(open('./chalicelib/data/words_dictionary.json').read())

        for word in data.keys():
            self.add(word)

        print("--- Initialized Trie in %s seconds ---" % (time.time() - start_time))

    def __str__(self):
        return self.char

    def add(self, word: str) -> None:
        # print('Adding {0}'.format(word))
        current_node = self

        for char in word:
            if char in current_node.children:
                child = current_node.get_child(char)
            else:
                child = TrieNode(char)
                current_node.add_child(child)

            current_node = child

        current_node.set_word(word)

    def find_word_node(self, word: str) -> TrieNode:
        top_node = self

        for letter in word:
            child = top_node.get_child(letter)

            if child is not None:
                top_node = child
            else:
                return None

        return top_node

    def word_has_children(self, prefix) -> bool:
        word_node = self.find_word_node(prefix)

        return word_node.children

    def is_word_exists(self, word: str) -> bool:
        word_node = self.find_word_node(word)

        return word_node.word == word
