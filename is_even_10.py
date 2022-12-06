# Challenge: Is the number even?
# Create a function called is_even that returns True if a given integer is
# even and False if it's not.


def is_even(num):
  if num % 2 == 0:
    return True
  else:
    return False


assert(is_even(2) == True)
assert(is_even(3) == False)