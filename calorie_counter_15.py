# Challenge: Calorie counter.
# Create a function called calorie_counter that accepts a dictionary of foods
# and their calories, and returns the total calories.

def calorie_counter(foods):
  total = sum(foods.values())
  return total


# Tests:
assert calorie_counter({'milk': 150, 'skim-milk': 100, 'almond-milk': 100}) == 350
assert calorie_counter({'eggs': 160, 'bacon': 200, 'toast': 80, 'coffee': 0}) == 440
