# Challenge: Any number to nine
# Create a function called any_number_to_nine that outputs a string between any number and 9.
# If the number being passed is greater than 9, return the string "0".
# Hint: Very similar to zero_to_nine, except the first number could be any number from 0-9.

def any_number_to_nine(num):
  return "0"


# Tests:
assert any_number_to_nine(0) == "0123456789"
assert any_number_to_nine(8) == "89"
assert any_number_to_nine(10) == "0"