# Challenge: Count the letter x, case insensitive
# Create a function called count_x that returns the number of "x" or "X" chracters in a string.
# Hint: The same as count_x.py, except it should work for upper and lower case.
# Hint: Consider converting the string to lower case every time so you never have to deal with "X"

def count_x(the_string):
  return 0

# Tests -- don't delete anything below this line!
assert count_x("xyz") == 1
assert count_x("Xyzx") == 2
assert count_x("yz") == 0
assert count_x("xxxxXxxxxX") == 10
