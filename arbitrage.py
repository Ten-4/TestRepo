
class Arbitrage_Engine(object):
	
	def __init__(self):
		raise NotImplementedError

	def push_orders(self, orders):
		#order is of the form ["ts:exchange:stock:price:buy/sell_sticker",...]
		raise NotImplementedError
		
	def execute(self):
		#Finds all arbitrage opportunities in the given set of orders.
		#of the form [ (ts, buy_order, sell_order)...]
		raise NotImplementedError
