import Constant
from __future__ import print_function

import sys
import socket

def connect(port=20000):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("test-exch-{}".format(Constant.teamname), port))
	return s.makefile('w+', 1)

def main():
	exchange = connect()
	print("HELLO TEAMNAME", file=exchange)
	hello_from_exchange = exchange.readline().strip()
	print("The exchange replied:", hello_from_exchange, file=sys.stderr)

if __name__ == "__main__":
	main()