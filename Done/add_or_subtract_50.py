# Challenge: Add or subtract
# Create a function called add_or_subtract that accepts two integers and a string representing either plus or minus, and does the correct calculation.
# For example, add_or_subtract(2, 1, "+") should return 3 and add_or_subtract(3, 1, "-") should return 2.


def add_or_subtract(first_int, second_int, operator):
  if operator == "+":
    sum = first_int + second_int
    return sum
  elif operator == "-":
    minus = first_int - second_int
    return minus


# Tests:
assert add_or_subtract(1, 1, "+") == 2
assert add_or_subtract(100, 2, "-") == 98
