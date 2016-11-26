from __future__ import print_function

import sys
import time
import json
import socket
import thread
import argparse
import Queue
import Constant

FP = None


def connect(port, istest):
	global FP
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = 'production'
	if istest:
		host = "test-exch-{}".format(Constant.TEAMNAME)
	s.connect((host, port))
	FP = s.makefile('w+', 1)


def tread():
	global FP
	return FP.readline().strip()

def readall():
	lines = []
	line = FP.readline()
	while line:
		lines.append(line)
		if FP.tell() <= 0:
			break
	return lines

def twrite(contentDict):
	global FP
	cmd = json.dumps(contentDict)
	print(cmd, file=FP)

def upload(contentDict):
	resp = twrite(contentDict)
	return resp


def hello():
	twrite(Constant.MSG_HELLO)
	
def update_msg():
	while True:
		
		for line in lines:
			MSGS.put(line)
		time.sleep(1)
		
def get_msgs():
	msgs = []
	while MSGS.qsize() > 0:
		line = MSGS.get()
		print(line)
		msgs.append(line)
	return msgs
	
def start(port, istrue):
	connect(port, istrue)
	thread.start_new_thread ( update_msg, () )

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='data process')
	# parser.add_argument('--port', '-p', action="store_true", help='fast load data')
	# parser.add_argument('--load', action="store_true", help='reload data, else load from cache')
	parser.add_argument('--port', '-p', type=int, help='port', default=25000)
	args = parser.parse_args()

	connect(args.port)
	resp = upload({"type": "add", "order_id": 1, "symbol": "BOND", "dir": "BUY", "price": 950, "size": 5})
	print(resp)
	
