# Challenge: Young or old
# Create a function called print_how_old that accepts an array of ages and
# prints "<age> is young" if the age is under 40, "<age> is old" if it's over 
# 40 and "<age> is ancient" if over 70.
#
# For example, if the age is 24 the function should print "24 is young".
#
# HINT: Don't forget to convert the integer to a string when printing it.


def print_how_old(ages):
  for age in ages:
    if age < 40:
      print(str(age) + " is young")
    elif age > 40 and age < 70:
      print(str(age) + " is old")
    elif age > 70:
      print(str(age) + " is ancient")


# Test:

# Assuming an array like this:

# [5, 42, 100]

# The function should print this:

# 5 is young
# 42 is old
# 100 is ancient

print_how_old([5, 42, 100])

