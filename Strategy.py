import Movement

HISTORICAL_LOOK_FORWARD = 100


def get_current_book(symbol):
    return []


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


def should_buy(our_order, current_avg, current_book):
    num = 0
    for order in our_order:
        if order["dir"] == "BUY" and order["prize"] == current_book["buy"][0]:
            return False
    return True


def should_sell(our_order, current_avg, current_book):
    num = 0
    for order in our_order:
        if order["dir"] == "SELL" and order["prize"] < current_book["sell"][0]:
            Movement.cancel(order["order_id"])
    for order in our_order:
        if order["dir"] == "SELL" and order["prize"] == current_book["sell"][0]:
            return False
    return True



def run_strategy(current_book, our_order, historical_trade):
    if len(current_book["buy"]) == 0 or len(current_book["sell"]) == 0:
        return
    current_avg = (current_book["buy"][0][0] + current_book["sell"][0][0]) / 2
    fair_price = get_fair_price(current_book, historical_trade)

