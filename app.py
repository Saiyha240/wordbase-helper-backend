import json

from chalice import Chalice

from chalicelib.trie import TrieBase

app = Chalice(app_name='wordbase-helper-backend')


def get_dictionary() -> TrieBase:
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
