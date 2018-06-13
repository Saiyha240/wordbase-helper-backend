class TrieNode(object):

    def __init__(self, char: str) -> None:
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1
        self.word = None

    def __str__(self) -> str:
        return self.char


class TrieBase(TrieNode):

    def __init__(self) -> None:
        super().__init__('*')

    def __str__(self):
        return self.char

    def add(self, word: str) -> None:
        # print('Adding {0}'.format(word))
        current_node = self

        for char in word:
            found_in_child = False

            for child in current_node.children:
                if child.char == char:
                    found_in_child = True
                    child.counter += 1
                    current_node = child
                    break

            if not found_in_child:
                new_child = TrieNode(char)
                current_node.children.append(new_child)
                current_node = new_child

        current_node.word_finished = True
        current_node.word = word

    def find_word_node(self, word: str) -> TrieNode:
        top_node = self

        for letter in word:
            child = next((x for x in top_node.children if letter == x.char), None)

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
