# Challenge: Pounds to kilos
# Create a function called pounds_to_kilos that converts a number from pounds to kilos.
# The function should return a value that is rounded up to the nearest 2 decimal points. 
# So rather than returning 5.91234 it should return 4.92.
# Hint a kilo is 0.453592 pounds. Do NOT round this amount. Only round the final output of the function.
# Hint: Similar to kilos_to_pounds.py

def pounds_to_kilos(x):
  kilos = x * 0.453592
  return round(kilos, 2)

# Tests -- don't delete anything below this line!
assert pounds_to_kilos(1) == 0.45
assert pounds_to_kilos(10) == 4.54

