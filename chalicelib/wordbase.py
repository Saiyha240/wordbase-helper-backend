from chalicelib.trie import TrieBase


class Tile(object):
    def __init__(self, char: str, x: int, y: int, marked: bool = False) -> None:
        self.char = char
        self.x = x
        self.y = y
        self.marked = marked
        self.adjacent_tiles = []

    def __str__(self) -> str:
        return self.char

    def set_adjacent_tiles(self, row_count: int, column_count: int):
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                adj_x = self.x + i
                adj_y = self.y + j

                if (i != 0 or j != 0) and (0 <= adj_x <= column_count and 0 <= adj_y <= row_count):
                    self.adjacent_tiles.append((adj_x, adj_y))

    @property
    def position(self) -> tuple([int, int]):
        return tuple([self.x, self.y])


class Word(object):

    def __init__(self) -> None:
        self.letters = []

    def get_word(self):
        return ''.join(letter.char for letter in self.letters)

    def __str__(self) -> str:
        return self.get_word()


class WordBase(object):
    def __init__(self, data: str, marked_map: list = [], dictionary: TrieBase = None, rows: int = 13,
                 columns: int = 10) -> None:
        self.tiles = {}
        self.rows = rows
        self.columns = columns
        self.marked_map = marked_map
        self.dictionary = dictionary
        self.data = data
        self.words = []

        self._set_tiles()
        self._mark_tiles()

    def _set_tiles(self):
        for row_num in range(0, self.rows):
            for col_num in range(0, self.columns):
                char = self.data[row_num * self.columns + col_num]
                tile = Tile(char, col_num, row_num)

                tile.set_adjacent_tiles(self.rows, self.columns)

                self.tiles[(tile.x, tile.y)] = tile

    def _mark_tiles(self):
        for marked in self.marked_map:
            if (marked['xCoor'], marked['yCoor']) in self.tiles:
                self.tiles[(marked['xCoor'], marked['yCoor'])].marked = True

    def print(self):
        for row in range(self.rows):
            for column in range(self.columns):
                tile = self.tiles[(column, row)]

                str_out = '-{0}- ' if tile.marked else '({0}) '

                print(str_out.format(self.tiles[(row, column)]), end='')
            print()
