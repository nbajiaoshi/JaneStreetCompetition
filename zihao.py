import json

BOOK_DICT = {}

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

def parse_message(line):
	dic = json.loads(line)
	if dic['type'] == 'book':
		BOOK_DICT[dic['symbol']]['SELL'] = dic['sell']
		BOOK_DICT[dic['symbol']]['BUY'] = dic['buy']