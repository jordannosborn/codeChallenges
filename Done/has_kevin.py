# Challenge: Has Kevin
# Create a function called has_kevin that returns True if a string has the substring "Kevin" in it and False if it doesn't.
# Hint: A substring is part of a string. For example, "BCD" is a substring of "ABCDEFG" and "Kevin" is a substring of "Kevin Sean Osborn"

def has_kevin(the_string):
  substring = "Kevin"
  if substring in the_string:
    return True
  else:
    return False

# Tests -- don't delete anything below this line!
assert has_kevin("Kevin Osborn") == True
assert has_kevin("Jude Osborn") == False
assert has_kevin("Kevin") == True
assert has_kevin("blah blah blah") == False
assert has_kevin("Where the fuck is Kevin?") == True