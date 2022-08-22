# Challenge: Has string
# Create a function called has_string that returns True if a string has a substring.

def has_kevin(the_string, substring):
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