from arbitrage import Arbitrage_Engine

def test_init():
	AE = Arbitrage_Engine()

def test_simple_arbitrage():
	AE = Arbitrage_Engine()
	orders = ["1:NYSE:AAPL:220.00:S","2:NASDAQ:AAPL:220.20:B"]
	AE.push_orders(orders)
	res = AE.execute()
	ans = [(2,"2:NASDAQ:AAPL:220.20:B","1:NYSE:AAPL:220.00:S")]
	assert ans == res

def test_A():
	pass

def test_B():
	pass

def test_C():
	pass

def test_D():
	pass
	
	
#/homes/ttp09/.local/lib/python2.7/site-packages