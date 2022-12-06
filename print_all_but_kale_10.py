# Challenge: Print all kale
# Create a function called print_all_but_kale that prints each value in an
# array of strings as long as the value is not "kale"


def print_all_but_kale(the_array):
  for x in the_array:
    if x != "kale":
      print(x)
    

# Assuming an array like this:

# ["pizza", "kale", "donut"]

# The function should print this:

# pizza
# donut

print_all_but_kale(["pizza", "kale", "donut"])