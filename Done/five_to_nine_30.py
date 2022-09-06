# Challenge: Five to nine
# Create a function called five_to_nine that creates a string with the numbers from 5 to 9.
# The function must use a loop. You can't just return "56789". :)
# Hint: Consider range().
# Hint: You might need to convert the integer to a string.l

def five_to_nine():
  output = ""
  for x in range(5, 10):
    output = output + str(x)
  return output

# Tests:
assert five_to_nine() == "56789"

