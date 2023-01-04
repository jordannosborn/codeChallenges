# Challenge: Cheap jeans
# Create a function called cheap_jeans that accepts a dictionary of
# clothing items and their prices, and returns True there are any 
# jeans at all that are $30 or cheaper.
#
# HINT: You'll need the key and the value in order to check if the 
# current item is "jeans".


def cheap_jeans(clothing):
  for key, value in clothing.items():
    if key == "jeans" and value <= 30:
        return True
  return False


# Tests:
assert cheap_jeans({'crop-top': 59, 'jeans': 30, 'leather-shoes': 340}) == True
assert cheap_jeans({'socks': 4, 'sandals': 24, 'hat': 44}) == False
assert cheap_jeans({'leather-jacket': 533, 'polo-shirt': 124, 'jeans': 350}) == False

