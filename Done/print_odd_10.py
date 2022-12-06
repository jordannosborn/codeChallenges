# Challenge: Print odd
# Create a function called print_odd that prints each element of an
# that is an odd number.


def print_odd(the_array):
  for x in the_array:
    if x % 2 != 0:
      print(x)



# Assuming an array like this:

# [3, 4, 5, 6, 7]

# The function should print this:

# 3
# 5
# 7

print_odd([3, 4, 5, 6, 7])
