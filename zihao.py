import json

def init_books():
	none_dict = {'buy': [], 'sell': []}
	init_dict = {'BOND': none_dict,
				 'VALBZ': none_dict,
				 'VALE': none_dict,
				 'GS': none_dict,
				 'MS': none_dict,
				 'WFC': none_dict,
				 'XLF': none_dict, 
	}
	return init_dict

BOOK = init_books()

def parse(msg):
	global BOOK
	msg = json.loads(msg)
	mtype = msg['type']
	if mtype == 'book':
		symbol = str(msg['symble'])
		BOOK[symbol]['sell'] = msg['sell']
		BOOK[symbol]['buy'] = msg['buy']
		print(BOOK)
	else:
		pass

