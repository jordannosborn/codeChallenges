# Challenge: Print any to any
# Create a function called print_any_to_any accepts two numbers are parameters and prints those numbers in order, one line at a time.


def print_any_to_any(num1, num2):
  for x in range(num1, num2 + 1):
    print(x)


# If you use 5 and 10 as parameters you'll need to be sure the output looks exactly like this:
# 5
# 6
# 7
# 8
# 9
# 10
print_any_to_any(5, 10)
