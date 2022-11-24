# Challenge: Print even
# Create a function called print_even that prints each element of an
# that is an even number.


def print_even(the_array):
  for x in the_array:
    if x % 2 == 0:
      print(x)


    

# Assuming an array like this:

# [3, 4, 5, 6, 7]

# The function should print this:

# 4
# 6


print_even([3, 4, 5, 6, 7])
