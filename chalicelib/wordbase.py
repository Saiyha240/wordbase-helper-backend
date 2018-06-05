class Letter(object):
    def __init__(self, char: str, x_coor: int, y_coor: int) -> None:
        self.char = char
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.adjacent_letters = []

    def add_adjacent_letter(self, letter_obj):
        self.adjacent_letters.append(letter_obj)


class WordBase(object):
    def __init__(self, data: str, rows: int = 13, columns: int = 10) -> None:
        self.tiles = {}
        self.rows = rows
        self.columns = columns
        self.data = data

    def add_tile(self, letter: Letter):
        letter.adjacent_letters = [(letter.x_coor + i, letter.y_coor + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if
                                   i != 0 or j != 0]
        self.tiles[(letter.x_coor, letter.y_coor)] = letter
