# Challenge: Food and toiletries total.
# Create a function called food_and_toiletries_total that accepts a dictionary 
# of food and another dictionary of toiletries, and returns the combined price 
# of all items.
#
# HINT: The prices are integers so you don't need to worry about decimal points 
# and currency conversion.


def food_and_toiletries_total(food, toiletries):
  total = 0
  food_total = 0
  toiletries_total = 0
  for key, value in food.items():
    food_total += value
  for key, value in toiletries.items():
    toiletries_total += value
  total = toiletries_total + food_total
  return total


# Tests:
assert food_and_toiletries_total({'eggs': 5, 'milk': 2}, {'shampoo': 6, 'toothbrush': 2}) == 15
assert food_and_toiletries_total({'bread': 2, 'bananas': 3, 'peanut-butter': 4}, {'conditioner': 5}) == 14
