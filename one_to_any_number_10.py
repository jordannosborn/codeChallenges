# Challenge: 1 to any number
# Create a function called one_to_any_number that outputs a string between 1 and any number.

def one_to_any_number(num):
  output = ""
  for x in range(1, num + 1):
    output = output + str(x)
  return output

# Tests:
assert one_to_any_number(5) == "12345"
assert one_to_any_number(3) == "123"
assert one_to_any_number(1) == "1"