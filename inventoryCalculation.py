prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

""" Printing inventory prices and cost """

for key in prices:
    print(key)
    print("price: %s" % prices[key])
    print("stock: %s \n" % stock[key])

""" Account for inventory value """
total = 0
for key in prices:
    total += prices[key] * stock[key]
print(total)
