# Challenge: Ballin
# Create function called ballin that accepts an integer, multiplies it by 100 and converts it from USD dollars to Australian dollars.
# Hint: 1 US dollar is 1.47 Australian dollars.

def ballin(us_dollars):
  dollars100 = us_dollars * 100
  dollars = dollars100 * 1.47
  return dollars


# Tests:
assert ballin(1) == 147
assert ballin(10) == 1470
assert ballin(500) == 73500