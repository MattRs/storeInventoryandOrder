""" Continued from inventoryCalculations """

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

""" Determine cost of shopping list """
shopping_list = ["banana", "orange", "apple"]

def compute_bill(food):
    total = 0
    for key in food:
        if stock[key] > 0:
            total += prices[key]
            stock[key] -= 1
    return total

compute_bill(shopping_list)
print(compute_bill(shopping_list))
