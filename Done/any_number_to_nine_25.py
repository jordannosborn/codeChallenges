# Challenge: Any number to nine
# Create a function called any_number_to_nine that outputs a string between any number and 9.
# If the number being passed is greater than 9, return the string "0".
# Hint: Very similar to zero_to_nine, except the first number could be any number from 0-9.

def any_number_to_nine(num):
  if num > 9:
    return "0"
  the_string = ""
  for n in range(num, 10):
    the_string = the_string + str(n)
  return the_string


# Tests:
assert any_number_to_nine(0) == "0123456789"
assert any_number_to_nine(8) == "89"
assert any_number_to_nine(10) == "0"