# Challenge: No fries
# Create a function called no_fries that accepts an array of ingredients that
# represent a meal, and returns true if the meal does not include fries.


def no_fries(meal):
  return False


# Tests:
assert no_fries(['chicken burger', 'french fries', 'chicken fingers']) == True
assert no_fries(['portuguese chicken', 'pita bread', 'greek salad']) == False
assert no_fries(['spheghetti sauce', 'pasta', 'raw carrots']) == False
