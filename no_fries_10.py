# Challenge: No fries
# Create a function called no_fries that accepts an array of ingredients that
# represent a meal, and returns true if the meal does not include fries.


def no_fries(meal):
  for food in meal:
    if "fries" in food:
      return False
  return True


# Tests:
assert no_fries(['chicken burger', 'french fries', 'chicken fingers']) == False
assert no_fries(['portuguese chicken', 'pita bread', 'greek salad']) == True
assert no_fries(['spheghetti sauce', 'pasta', 'raw carrots']) == True
