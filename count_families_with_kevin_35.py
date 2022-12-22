# Challenge: Count families with Kevin
# Create a function called count_families_with_kevin that counts the number of
# families that have a Kevin.
# count_families_with_kevin() will accept a parameter that is an array of
# families, so this means you will need to deal with a 2 dimensional array
# (aka an array of arrays). 
#
# Hint: Keep in mind that in Python an "Array" is often referred to as a "List". Same 
# thing.
# Hint: This link might help you:
# https://medium.com/an-amygdala/how-to-iterate-through-a-2d-list-in-python-5a90693f3a15


def count_families_with_kevin(families):
  total = 0
  for family in families:
      if name == "Kevin":
        total += 1
  return total

# Tests:
assert count_families_with_kevin([['Kevin', 'Jude', 'Amie', 'Jordann'], ['Bob', 'Sara', 'Jane'], ['Doug', 'Kevin', 'Raj']]) == 2
assert count_families_with_kevin([['Bob', 'Sara', 'Jane'], ['Doug', 'Raj']]) == 0
