import json


def init_books():
    none_dict = {'BUY': [], 'SELL': []}
    init_dict = {'BOND': none_dict,
                 'VALBZ': none_dict,
                 'VALE': none_dict,
                 'GS': none_dict,
                 'MS': none_dict,
                 'WFC': none_dict,
                 'XLF': none_dict,
                 }
    return init_dict


BOOK_DICT = init_books()
HELLO_DICT = None


def parse_message(line):
    dic = json.loads(line)
    if dic['type'] == 'book':
        BOOK_DICT[str(dic['symbol'])]['sell'] = dic['sell']
        BOOK_DICT[str(dic['symbol'])]['buy'] = dic['buy']
    if dic['type'] == 'hello':
        HELLO_DICT = dic
        print(HELLO_DICT)
