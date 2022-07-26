# Challenge: Jeepers score
# Create a function called jeepers_score that returns the number of times the word "jeepers" appears in a string.
# The function should be case insensitive, which means it works regardless of upper or lower case. So "Jeepers" counts, as does "JEEPers" and "JeeperS".
# Hint: Consider converting to lower case before counting.


def jeepers_score(the_string):
  return 0


# Tests:
assert jeepers_score("Jeepers jEEpers jeepers JEEPERS") == 4
assert jeepers_score("creepers") == 0
