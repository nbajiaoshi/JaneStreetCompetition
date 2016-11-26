from __future__ import print_function

import time
import json
import argparse

import Constant
from TCP import *
from zihao import *


def add(order_id, symbol, direction, price, size):
	cmd = {"type": "add", "order_id": order_id, "symbol": symbol, "dir": direction, "price": price, "size": size}
	upload(cmd)
	return cmd


def convert(order_id, symbol, direction, size):
	cmd = {"type": "convert", "order_id": order_id, "symbol": symbol, "dir": direction, "size": size}
	upload(cmd)
	return cmd


def cancel(order_id):
	cmd = {"type": "cancel", "order_id": order_id}
	upload(cmd)
	return cmd


def buy(order_id, symbol, price, size):
	print('buying:', order_id, symbol, price, size)
	cmd = add(order_id, symbol, 'BUY', price, size)
	ORDERS[symbol].append(cmd)
	return cmd


def sell(order_id, symbol, price, size):
	print('selling:', order_id, symbol, price, size)
	cmd = add(order_id, symbol, 'SELL', price, size)
	ORDERS[symbol].append(cmd)
	return cmd

def init():
	parser = argparse.ArgumentParser(description='data process')
	parser.add_argument('--port', '-p', type=int, help='port', default=25000)
	parser.add_argument('--istest', '-t', action="store_true", help='reload data, else load from cache')
	args = parser.parse_args()

	connect(args.port, args.istest)
	print('connect ok')
	hello()
	print(readall)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='data process')
	parser.add_argument('--port', '-p', type=int, help='port', default=25000)
	parser.add_argument('--istest', '-t', action="store_true", help='reload data, else load from cache')
	args = parser.parse_args()
	
	connect(args.port, args.istest)
	print('connect ok')
	hello()
	