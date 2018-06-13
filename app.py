import json
import time

from chalice import Chalice

from chalicelib.trie import TrieBase
from chalicelib.wordbase import WordBase

app = Chalice(app_name='wordbase-helper-backend')


def get_dictionary() -> TrieBase:
    start_time = time.time()

    data = json.loads(open('./chalicelib/data/words_dictionary.json').read())
    root = TrieBase()

    for word in data.keys():
        root.add(word)

    print("--- Initialized Trie in %s seconds ---" % (time.time() - start_time))

    return root


@app.route('/', methods=['POST'])
def index():
    request = app.current_request.json_body

    wb = WordBase(request['cellsString'], request['markedMap'], get_dictionary())

    return wb.get_answers()
