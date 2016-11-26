from time import sleep

import Movement
from Constant import *
from zihao import BOOK

HISTORICAL_LOOK_FORWARD = 100
TRANSACTION_SIZE = 3

current_order_id = 65487


def get_current_book(symbol):
	return BOOK[symbol]


def get_historical_trade(symbol):
	return []


def get_our_order(symbol):
	return []


def get_fair_price(current_book, historical_trade):
	sum = 0
	num = 0
	for i in range(max(0, len(historical_trade) - HISTORICAL_LOOK_FORWARD), len(historical_trade)):
		sum += historical_trade[i]["price"] * historical_trade[i]["size"]
		num += historical_trade[i]["size"]
	historical_avg = sum / num
	return historical_avg


def should_buy(our_order, current_book):
	return True
	for order in our_order:
		if order["dir"] == "BUY" and order["prize"] == current_book["buy"][0]:
			return False
	return True


def should_sell(our_order, current_book):
	return True
	for order in our_order:
		if order["dir"] == "SELL" and order["prize"] > current_book["sell"][0] + 5:
			Movement.cancel(order["order_id"])
	for order in our_order:
		if order["dir"] == "SELL" and order["prize"] == current_book["sell"][0]:
			return False
	return True


def buy_current_price(symbol, current_book):
	global current_order_id
	current_order_id += 1
	Movement.buy(current_order_id, symbol, current_book["buy"][0], TRANSACTION_SIZE)


def buy_higher_price(symbol, current_book):
	global current_order_id
	current_order_id += 1
	Movement.buy(current_order_id, symbol, current_book["buy"][0] + 1, TRANSACTION_SIZE)


def sell_current_price(symbol, current_book):
	global current_order_id
	current_order_id += 1
	Movement.buy(current_order_id, symbol, current_book["sell"][0], TRANSACTION_SIZE)


def sell_lower_price(symbol, current_book):
	global current_order_id
	current_order_id += 1
	Movement.buy(current_order_id, symbol, current_book["sell"][0] - 1, TRANSACTION_SIZE)


def run_strategy(symbol, current_book, our_order, historical_trade):

	if len(current_book["buy"]) == 0 or len(current_book["sell"]) == 0:
		return
	current_avg = (current_book["buy"][0][0] + current_book["sell"][0][0]) / 2
	# fair_price = get_fair_price(current_book, historical_trade)
	if should_buy(our_order, current_book):
		buy_current_price(symbol, current_book)
	if should_sell(our_order, current_book):
		sell_current_price(symbol, current_book)


if __name__ == '__main__':
	Movement.init()
	while True:
		for stock_symbol in STOCK_NAME:
			run_strategy(stock_symbol, get_current_book(stock_symbol),
						 get_our_order(stock_symbol), get_historical_trade(stock_symbol))
		sleep(0.05)




