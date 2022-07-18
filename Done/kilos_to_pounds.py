# Challenge: Kilos to Pounds
# Create a function called kilos_to_pounds that converts a number from kilos to pounds.
# The function should return a value that is rounded up to the nearest 2 decimal points. 
# So rather than returning 5.91234 it should return 4.92.
# Hint a pounds is 2.20462 kilos. Do NOT round this amount. Only round the final output of the function.
# Hint: Python has a very simple function that takes care of the rounding.

def kilos_to_pounds(x):
  pounds = x * 2.2046
  return round(pounds, 2)

# Tests -- don't delete anything below this line!
assert kilos_to_pounds(200) == 440.92
assert kilos_to_pounds(10) == 22.05
assert kilos_to_pounds(50000) == 110230.0
assert kilos_to_pounds(34) == 74.96
