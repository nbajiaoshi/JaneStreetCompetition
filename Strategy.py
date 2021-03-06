from time import sleep

import Movement
from Constant import *
from zihao import *

HISTORICAL_LOOK_FORWARD = 10000
TRANSACTION_SIZE = 20

current_order_id = 65487


def get_current_book(symbol):
	return BOOK[symbol]


def get_historical_trade(symbol):
	return TRADE[symbol]


def get_our_order(symbol):
	return ORDERS[symbol]


def get_fair_price(current_book, historical_trade):
	sum = 0.0
	num = 0.0
	for i in range(max(0, len(historical_trade) - HISTORICAL_LOOK_FORWARD), len(historical_trade)):
		sum += historical_trade[i][0] * historical_trade[i][1]
		num += historical_trade[i][1]
	historical_avg = sum / num
	return historical_avg


def should_buy(our_order, current_book):
	for order in our_order:
		if order["dir"] == "BUY" and order["price"] == current_book["buy"][0][0]:
			return False
	return True


def should_sell(our_order, current_book):
	for order in our_order:
		if order["dir"] == "SELL" and order["price"] > current_book["sell"][0][0] + 5:
			Movement.cancel(order["order_id"])
	for order in our_order:
		if order["dir"] == "SELL" and order["price"] == current_book["sell"][0][0]:
			return False
	return True


def buy_current_price(symbol, current_book):
	global current_order_id
	current_order_id += 1
	Movement.buy(current_order_id, symbol, current_book["buy"][0][0], TRANSACTION_SIZE)


def buy_higher_price(symbol, current_book):
	global current_order_id
	current_order_id += 1
	Movement.buy(current_order_id, symbol, current_book["buy"][0][0] + 1, TRANSACTION_SIZE)


def sell_current_price(symbol, current_book):
	global current_order_id
	current_order_id += 1
	Movement.sell(current_order_id, symbol, current_book["sell"][0][0], TRANSACTION_SIZE)


def sell_lower_price(symbol, current_book):
	global current_order_id
	current_order_id += 1
	Movement.sell(current_order_id, symbol, current_book["sell"][0][0] - 1, TRANSACTION_SIZE)


def run_strategy(symbol, current_book, our_order, historical_trade):
	try:
		if len(current_book["buy"]) == 0 or len(current_book["sell"]) == 0:
			return
		current_avg = (current_book["buy"][0][0] + current_book["sell"][0][0]) / 2
		fair_price = get_fair_price(current_book, historical_trade)
		if should_buy(our_order, current_book) and current_book["buy"][0][0] < fair_price:
			if current_book["buy"][0][0] < fair_price - 2:
				buy_current_price(symbol, current_book)
			else:
				buy_higher_price(symbol, current_book)
		if should_sell(our_order, current_book) and current_book['sell'][0][0] > fair_price:
			if current_book['buy'][0][0] < IN_PRICE[symbol]:
				pass
			elif current_book['sell'][0][0] > fair_price + 2:
				sell_current_price(symbol, current_book)
			else:
				sell_lower_price(symbol, current_book)
	except Exception as e:
		print(e)


if __name__ == '__main__':
	Movement.init()
	while True:
		for stock_symbol in STOCK_NAME:
			run_strategy(stock_symbol, get_current_book(stock_symbol),
						 get_our_order(stock_symbol), get_historical_trade(stock_symbol))
		sleep(0.05)
