# Challenge: Has chicken
# Create a function called has_chicken that accepts an array of
# ingredients that represent a meal, and returns true if chicken is
# anywhere in the meal, and false if it's not.


def has_chicken(meal):
  for food in meal:
    if "chicken" in food:
      return True
    else:
      return False


# Tests:
assert has_chicken(['portuguese chicken', 'pita bread', 'greek salad']) == True
assert has_chicken(['chicken burger', 'french fries', 'chicken fingers']) == True
assert has_chicken(['spheghetti sauce', 'pasta', 'raw carrots']) == False
