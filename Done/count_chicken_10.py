# Challenge: Count chicken
# Create a function called count_chicken that accepts an array of ingredients
# that represent a meal, and returns the number of ingredients that have 
# chicken.


def count_chicken(meal):
  total = 0
  for food in meal:
    if "chicken" in food:
      total += 1
  return total


# Tests:
assert count_chicken(['portuguese chicken', 'pita bread', 'greek salad']) == 1
assert count_chicken(['chicken burger', 'french fries', 'chicken fingers']) == 2
assert count_chicken(['spheghetti sauce', 'pasta', 'raw carrots']) == 0
