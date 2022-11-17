# Challenge: Print "odd" or "even"
# Create a function called print_odd_even that accepts an array of integers and
# prints "odd" if the integer is odd and "even" if it's even


def print_odd_even(the_array):
  for x in the_array:
    if x % 2 == 0:
      print("even")
    else:
      print("odd")
    

# Assuming an array like this:

# [4, 3, 2, 50, 51]

# The function should print this:

# even
# odd
# even
# even
# odd

print_odd_even([4, 3, 2, 50, 51])