# list_comprehension_investigation.py

from random import shuffle


numbers = [1, 2, 5, 3, 6, 4, 8, 9, 7]

doubled_numbers = [n*2 for n in numbers]

print (numbers)
print (doubled_numbers)

names = ["alice", "bob", "carol", "dan"]
capitalised = [name.capitalize() for name in names]

print (names)
print (capitalised)

# use this to filter a list
numbers = [100, 750, 300, 95, 800, 150, 600]
big_numbers = [number for number in numbers if number > 500]

print (numbers)
print (big_numbers)

# works in 2 dimensions
colours = ["red", "green", "blue"]
products = ["pen", "pencil", "crayon"]

product_list = [f"{colour} {product}" for colour in colours for product in products]
print (product_list)


# playing cards
suits = ["H", "S", "D", "C"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

cards = [f" {value}{suit} " for suit in suits for value in values]
print (cards)

shuffle(cards)

for card in cards:
    print (card)

    
















