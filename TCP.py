from __future__ import print_function

import sys
import json
import socket
import thread
import argparse

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
<<<<<<< HEAD
	line = tread()
	while line:
		line = tread()
		print(line)
	
=======
    lines = []
    line = tread()
    while line:
        lines.append(line)
        line = tread()
    return lines


>>>>>>> 09196dac5174f06a9815970a4c5b6e35a7603690
def twrite(contentDict):
    global FP
    cmd = json.dumps(contentDict)
    print(cmd, file=FP)
    return json.loads(tread())


def upload(contentDict):
    respHello = twrite(Constant.MSG_HELLO)
    if contentDict is None:
        return respHello
    resp = twrite(contentDict)
    return resp


def hello():
<<<<<<< HEAD
	respHello = twrite(Constant.MSG_HELLO)
	return respHello
	
def start(port, istest):
	connect(port, istest)
	thread.start_new_thread ( readall )
=======
    respHello = twrite(Constant.MSG_HELLO)
    return respHello

>>>>>>> 09196dac5174f06a9815970a4c5b6e35a7603690

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='data process')
    # parser.add_argument('--port', '-p', action="store_true", help='fast load data')
    # parser.add_argument('--load', action="store_true", help='reload data, else load from cache')
    parser.add_argument('--port', '-p', type=int, help='port', default=25000)
    args = parser.parse_args()

    connect(args.port)
    resp = upload({"type": "add", "order_id": 1, "symbol": "BOND", "dir": "BUY", "price": 950, "size": 5})
    print(resp)
