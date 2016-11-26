from __future__ import print_function

import sys
import json
import socket
import argparse

import Constant

FP = None

def connect(port):
	global FP
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("test-exch-{}".format(Constant.teamname), port))
	FP = s.makefile('w+', 1)
	
def read():
	global FP
	return FP.readline().strip()
	
def write(contentDict):
	global FP
	cmd = json.dumps(contentDict)
	print(cmd, file=FP)
	return json.loads(read(FP))

def upload(contentDict):
	respHello = write(Constant.MSG_HELLO)
	respType = respHello['type']
	if respType['type'] != 'hello':
		return False
	resp = write(contentDict)
	return resp

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='data process')
	# parser.add_argument('--port', '-p', action="store_true", help='fast load data')
	# parser.add_argument('--load', action="store_true", help='reload data, else load from cache')
	parser.add_argument('--port', '-p', type=int, help='port', default=25000)
	args = parser.parse_args()
	
	connect(args.port)
	resp = upload({"type": "add", "order_id": 1, "symbol": "BOND", "dir": "BUY", "price": 950, "size": 5})
	print resp