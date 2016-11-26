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
ORDERS = {
			'BOND': [],
			 'VALBZ': [],
			 'VALE': [],
			 'GS': [],
			 'MS': [],
			 'WFC': [],
			 'XLF': [], 
}

POSITION = {
			'BOND': 0,
			 'VALBZ': 0,
			 'VALE': 0,
			 'GS': 0,
			 'MS': 0,
			 'WFC': 0,
			 'XLF': 0, 
}

IN_PRICE = {
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
	try:
		msg = json.loads(msg)
	except:
		return
	mtype = msg['type']
	if mtype == 'book':
		symbol = str(msg['symbol'])
		BOOK[symbol]['sell'] = msg['sell']
		BOOK[symbol]['buy'] = msg['buy']
	elif mtype == 'trade':
		symbol = str(msg['symbol'])
		try:
			price = int(msg['price'])
			size = int(msg['size'])
			TRADE[symbol].append((price, size))
			if len(TRADE[symbol]) > 100000:
				TRADE[symbol] = TRADE[symbol][-100000:]
		except Exception as e:
			print(msg)
			print(msg['price'], msg['size'])
			print('@parse {}'.format(e))
	elif mtype == 'fill':
		print(msg)
		symbol = str(msg['symbol'])
		direction = str(msg['dir'])
		orderid = int(msg['order_id'])
		for i, order in enumerate(ORDERS[symbol]):
			if order['order_id'] == orderid:
				ORDERS[symbol][i]['size'] -= int(msg['size'])
				break
		if direction == 'BUY':
			IN_PRICE[symbol] = int(msg['price'])
		else:
			print(msg['price'], IN_PRICE[symbol])
	elif mtype == 'ack':
		pass
	elif mtype == 'reject':
		pass
	elif mtype == 'out':
		pass
		
