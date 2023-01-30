# Challenge: Count shoe cost
# Create a function called count_shoe_cost that accepts a dictionary of
# clothing items and their prices, and returns the total cost of any items
# that contain the string "shoe". For example, both "leather-shoes" and 
# "shoes" should be counted.


def count_shoe_cost(clothing):
  total = 0
  for key, value in clothing.items():
    if "shoe" in key:
      total += value
  return total


# Tests:
assert count_shoe_cost({'crop-top': 59, 'jeans': 30, 'leather-shoes': 340}) == 340
assert count_shoe_cost({'socks': 4, 'sandals': 24, 'hat': 44}) == 0
assert count_shoe_cost({'leather-jacket': 500, 'tennis-shoes': 120, 'shoes': 100}) == 220

