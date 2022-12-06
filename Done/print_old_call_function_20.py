# Challenge: print old by calling a function
# This challenge is about calling a function inside a function.
# It requires two functions:
# 1. make_old(age), which multiplies an age by 10. You'll need to create this
# function yourself.
# 2. print_old(age), which calls make_old, passing an age to it, then printing 
# that age.
def make_old(age):
  old_age = age * 10
  return old_age


def print_old(age):
  new_age = make_old(age)
  print(new_age)


# Tests:

# First, let's make sure you've made a function called make_old that multiplies
# a given age by 10.
assert(make_old(10) == 100)
assert(make_old(2) == 20)

# Now let's see if print_old is calling make_old properly. If it is, then
# print_old(12) should print this:

# 120

print_old(12)
