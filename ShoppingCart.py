class product:
	def __init__(self, name = " ", price = 0):
		self.name = name
		self.price = price

class Basket:

    products = []

    def addItem(self, product,):
        self.products.append(product)

    def printProducts(self):
        for x in self.products:
            print(x.name, x.price)
      
          
_basket = Basket()

_movie1 = product('Star Wars directed by George Lucas', 40)
_movie2 = product('Django directed by Quinton Tarentino', 20)
_movie3 = product('Rocy directed by Sylvester Stallone', 10)

_basket.addItem(_movie1)
_basket.addItem(_movie2)
_basket.addItem(_movie3)

_basket.printProducts()

subTotal = _movie1.price + _movie2.price + _movie3.price
tax = 0.09
tax = 0.09 * subTotal
total = subTotal + tax

print("\nSub total: $" + format(subTotal, ",.2f"), "Tax amount: $" + \
    format(tax, ",.2f"), "Total: $" + format(total, ",.2f"), \
        sep = "\n" )




