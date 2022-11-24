# Challenge: Print reversed
# Create a function called print_reversed that reverses and prints each element
# in an array of strings. For example, "dude" becomes "edud".


def print_reversed(the_array):
  for x in the_array:
    print(x[::-1])
    

# Assuming an array like this:

# ["yo", "sup", "dude"]

# The function should print this:

# oy
# pus
# edud

print_reversed(["yo", "sup", "dude"])