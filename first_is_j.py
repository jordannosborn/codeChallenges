# Challenge: First character is j
# Create a function called first_is_j that returns True if the first character of a string is either lower case "j" or upper case "J".

def first_is_j(the_string):
  charsToMatch = ('j', 'J')
  the_string.startswith(charsToMatch)
  return True

# Tests -- don't delete anything below this line!
assert first_is_j("Jude") == True
assert first_is_j("Dude") == False
assert first_is_j("jelly") == True
assert first_is_j("belly") == False
