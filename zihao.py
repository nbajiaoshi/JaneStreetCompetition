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
	
def init_trades():
	init_dict = {'BOND': [],
				 'VALBZ': [],
				 'VALE': [],
				 'GS': [],
				 'MS': [],
				 'WFC': [],
				 'XLF': [], 
	}
	return init_dict

BOOK = init_books()
TRADE = init_trades()

POSITION = {
			'BOND': 0,
			 'VALBZ': 0,
			 'VALE': 0,
			 'GS': 0,
			 'MS': 0,
			 'WFC': 0,
			 'XLF': 0, 
}

'''
	key: order_id
	value:
		(1) {"type": "add", "order_id": N, "symbol": "SYM", "dir": "BUY", "price": N, "size": N}
		(2) {"type": "convert", "order_id": N, "symbol": "SYM", "dir": "BUY", "size": N}
		(3) {"type": "cancel", "order_id": N}
'''
order_dict = {}

def parse(msg):
	global BOOK
	msg = json.loads(msg)
	mtype = msg['type']
	if mtype == 'book':
		symbol = str(msg['symbol'])
		BOOK[symbol]['sell'] = msg['sell']
		BOOK[symbol]['buy'] = msg['buy']
	elif mtype == 'trade':
		symbol = str(msg['symbol'])
		try:
			TRADE[symbol].append((int(msg['price'], int(msg['size']))))
			if len(TRADE[symbol] > 1000):
				TRADE[symbol] = TRADE[symbol][-1000:]
		except:
			pass
	elif mtype == 'fill':
		symbol = str(msg['symbol'])
		direction = 2 * int(msg['dir'] == 'BUY') - 1
		POSITION[symbol] += direction * int(msg['size'])
	elif mtype == 'ack':
		pass
	elif mtype == 'reject':
		pass
	elif mtype == 'out':
		pass
		
