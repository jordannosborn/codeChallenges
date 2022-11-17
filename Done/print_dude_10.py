# Challenge: Print dude
# Create a function called print_dude that prints each element of 
# an array as long as that element is "dude".


def print_dude(the_array):
  for x in the_array:
    if x == "dude":
      print(x)
    

# Assuming an array like this:

# ["yo", "sup", "dude"]

# The function should print this:

# dude

print_dude(["yo", "sup", "dude"])