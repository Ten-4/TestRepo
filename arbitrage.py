
class Arbitrage_Engine(object):
	
	def __init__(self):
		raise NotImplemented
		
	def push_orders(self, orders):
		#order is of the form ["exchange:stock:price:buy/sell_sticker",...]
		raise NotImplemented
		
	def execute(self):
		arbs = []
		#Finds all arbitrage opportunities in the given set of orders.
		raise NotImplemented
		return arbs