# Challenge: Expensive items
# Create a function called expensive_items that accepts a dictionary of
# clothing items and their prices, and returns True if anything on the 
# list is over $300.


def expensive_items(clothing):
  return False


# Tests:
assert expensive_items({'crop-top': 59, 'jeans': 150, 'leather-shoes': 340}) == True
assert expensive_items({'socks': 4, 'sandals': 24, 'hat': 44}) == False
assert expensive_items({'leather-jacket': 533, 'polo-shirt': 124, 'fancy-pants': 344}) == True
