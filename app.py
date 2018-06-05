import json

from chalice import Chalice

from chalicelib.trie import TrieNode, TrieBase
from chalicelib.wordbase import WordBase, Letter

app = Chalice(app_name='wordbase-helper-backend')


def get_dictionary() -> TrieNode:
    data = json.loads(open('./chalicelib/data/words_dictionary.json').read())
    root = TrieBase()

    for word in data.keys():
        root.add(word)

    return root


@app.route('/', methods=['POST'])
def index():
    request = app.current_request.json_body

    dictionary = get_dictionary()

    return {'hello': 'world'}


data = {
    "rowCount": "13",
    "colCount": "10",
    "markedMap": [
        {
            "xCoor": 0,
            "yCoor": 0
        },
        {
            "xCoor": 1,
            "yCoor": 0
        },
        {
            "xCoor": 2,
            "yCoor": 0
        },
        {
            "xCoor": 3,
            "yCoor": 0
        },
        {
            "xCoor": 4,
            "yCoor": 0
        },
        {
            "xCoor": 5,
            "yCoor": 0
        },
        {
            "xCoor": 6,
            "yCoor": 0
        },
        {
            "xCoor": 7,
            "yCoor": 0
        },
        {
            "xCoor": 8,
            "yCoor": 0
        },
        {
            "xCoor": 9,
            "yCoor": 0
        }
    ],
    "cellsString": "ectrygamylkiehrantghtfpdodeistosfauidcpicetbroramerilgoemseraoncnutfgodecisgytasilotneirnclrfmarmscenatopmseliyliaryecsnwhlplrptum"
}

wb = WordBase(data['cellsString'])

for row_num in range(0, wb.rows):
    # print(row_num)
    for col_num in range(0, wb.columns):
        letter = wb.data[row_num * wb.columns + col_num]
        wb.add_tile(Letter(letter, row_num, col_num))
        # print(col_num)
        pass

print(wb)
