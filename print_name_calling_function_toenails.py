# Challenge: print last name by calling function
# This challenge is about calling a function inside a function.
# It requires two functions:
# 1. print_name(name), which accepts a first name and prints it.
# 2. add_osborn(name), accepts a first name and returns that name with
# "Osborn" appended to the end of it.
#
# HINT: Notice that add_osborn RETURNS a value but print_name PRINTS a value.


def add_osborn(name):
  return ''


def print_name(name):
  print('')


# Tests:

# First, let's make sure you've made a function called add_osborn that adds the
# last name.
assert(add_osborn('Jude') == 'Jude Osborn')
assert(add_osborn('Jordann') == 'Jordann Osborn')

# Now let's see if print_old is calling make_old properly. If it is, then
# print_name("Kevin") should print this:

# Kevin Osborn

print_name("Kevin")
