# Challenge: Shopping total
# Create a function called shopping_total that accepts a dictionary of 
# groceries and their prices, and returns the total cost of all items.
# Note that total should be rounded to the nearest two decimal points. 
# For example, of the total is 59.9345 it should be converted to 59.93.

def shopping_total(groceries):
  total = sum(groceries.values())
  round_total = round(total, 2)
  return round_total


# Tests:
assert shopping_total({'eggs': 4.99, 'milk': 1.50, 'shampoo': 6.54}) == 13.03
assert shopping_total({'cat-food': 24.99, 'snacky-snacks': 3.72}) == 28.71