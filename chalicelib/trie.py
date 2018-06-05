class TrieNode(object):

    def __init__(self, char: str) -> None:
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1

    def __str__(self) -> str:
        return self.char


class TrieBase(object):

    def __init__(self) -> None:
        self.char = '*'
        self.children = []
        self.word_finished = False

    def __str__(self):
        return self.char

    def add(self, word: str) -> None:
        print('Adding {0}'.format(word))
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
