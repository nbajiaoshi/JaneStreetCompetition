from zihao import *
from Constant import *
from TCP import *
from Strategy import *


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='data process')
	parser.add_argument('--port', '-p', type=int, help='port', default=25000)
	parser.add_argument('--istest', '-t', action="store_true", help='reload data, else load from cache')
	args = parser.parse_args()
	
	FP = connect(args.port, args.istest)
	print('connect ok')
	hello()
	
	
	while True:
		for i in range(1000):
			response = FP.readline()
			parse(response)
		for stock_symbol in STOCK_NAME:
			run_strategy(stock_symbol, get_current_book(stock_symbol),
						 get_our_order(stock_symbol), get_historical_trade(stock_symbol))
		
						 