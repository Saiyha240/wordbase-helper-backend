class Letter(object):
    def __init__(self, char: str, x_coor: int, y_coor: int) -> None:
        self.char = char
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.adjacent_letters = []

    def add_adjacent_letter(self, letter_obj):
        self.adjacent_letters.append(letter_obj)

    def __str__(self) -> str:
        return self.char


class WordBase(object):
    def __init__(self, data: str, rows: int = 13, columns: int = 10) -> None:
        self.tiles = {}
        self.rows = rows
        self.columns = columns
        self.data = data

    def add_tile(self, letter: Letter):
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                adj_x = letter.x_coor + i
                adj_y = letter.y_coor + j
                if (i != 0 or j != 0) and (0 <= adj_x <= self.columns and 0 <= adj_y <= self.rows):
                    letter.add_adjacent_letter((adj_x, adj_y))

        self.tiles[(letter.x_coor, letter.y_coor)] = letter

    def print(self):
        for row in range(self.rows):
            for column in range(self.columns):
                print('({0}) '.format(self.tiles[(row, column)]), end='')
            print()
