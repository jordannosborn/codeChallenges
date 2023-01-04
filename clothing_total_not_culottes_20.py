# Challenge: Clothing total not culottes
# Create a function called clothing_total_not_culottes that accepts a dictionary of and
# returns the total cost for all the items. Note that culottes and dumb and
# dorky so they should not be counted.
#
# HINT: You'll need the key to check if the item is culottes and the value to calculate
# the total.


def clothing_total_not_culottes(clothing):
  total = 0
  for key, value in clothing.items():
    if key != "culottes":
      total += value
  return total


# Tests:
assert clothing_total_not_culottes({'crop-top': 50, 'culottes': 700, 'leather-shoes': 50}) == 100
assert clothing_total_not_culottes({'socks': 5, 'sandals': 25, 'hat': 20}) == 50
