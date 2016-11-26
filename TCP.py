from __future__ import print_function

import sys
import time
import json
import socket
import thread
import argparse
import Queue
import Constant
import threading
import zihao

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
	return json.loads(FP.readline().strip())

def readall():
	lines = FP.readlines()
	return lines

def twrite(contentDict):
	global FP
	cmd = json.dumps(contentDict)
	print(cmd, file=FP)

def upload(contentDict):
	respHello = twrite(Constant.MSG_HELLO)
	if contentDict is None:
		return respHello
	resp = twrite(contentDict)
	return resp


def hello(tries=100):
	respHello = twrite(Constant.MSG_HELLO)
	return respHello
	
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
	
	
class myThread (threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self._stop = threading.Event()
		
	def run(self):
		try:
			while True:
				msg = FP.readline().strip()
				zihao.parse_message(msg)
		except KeyboardInterrupt:
			sys.exit(0)
		
	def stop(self):
		self._stop.set()


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='data process')
	# parser.add_argument('--port', '-p', action="store_true", help='fast load data')
	# parser.add_argument('--load', action="store_true", help='reload data, else load from cache')
	parser.add_argument('--port', '-p', type=int, help='port', default=25000)
	args = parser.parse_args()

	connect(args.port)
	resp = upload({"type": "add", "order_id": 1, "symbol": "BOND", "dir": "BUY", "price": 950, "size": 5})
	print(resp)
	
