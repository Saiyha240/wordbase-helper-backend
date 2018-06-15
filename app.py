from chalice import Chalice, CORSConfig

from chalicelib.trie import TrieBase
from chalicelib.wordbase import WordBase

app = Chalice(app_name='wordbase-helper-backend')
cors = CORSConfig()
app.debug = True
dictionary = TrieBase()


@app.route('/', methods=['POST'], cors=cors)
def index():
    request = app.current_request.json_body

    wb = WordBase(request['cellsString'], request['markedMap'], dictionary)

    return wb.get_answers()
