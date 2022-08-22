# Challenge: Has Kitty, not Kevin
# Create a function called has_kitty_not_kevin that returns True if a string has "Kitty" but not "Kevin"

def has_kevin(the_string):
  return False

# Tests -- don't delete anything below this line!
assert has_kevin("Kitty Osborn") == True
assert has_kevin("Kevin Osborn") == False
assert has_kevin("Kevin and Kitty") == False
assert has_kevin("Jude Osborn") == False
