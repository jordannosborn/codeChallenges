# Challenge: Print array adding 1 to even, 2 to odd
# Create a function called print_increment_odd_even that prints each element
# of an array of integers, adding 1 if the element is even and 2 if the 
# element is odd.


def print_increment_odd_even(the_array):
  for x in the_array:
    if x % 2 == 0:
      print(x + 1)
    else:
      print(x + 2)
    

# Assuming an array like this:

# [3, 4, 5, 6, 7]

# The function should print this:

# 5
# 5
# 7
# 7
# 9


print_increment_odd_even([3, 4, 5, 6, 7])
