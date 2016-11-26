from zihao import *
from Constant import *
from TCP import *


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='data process')
	parser.add_argument('--port', '-p', type=int, help='port', default=25000)
	parser.add_argument('--istest', '-t', action="store_true", help='reload data, else load from cache')
	args = parser.parse_args()
	
	connect(args.port, args.istest)
	print('connect ok')
	hello()
	
	while True:
		response = FP.readline()
		zihao.parse(response)