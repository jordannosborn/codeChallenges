# Challenge: Remove Spaces
# Create a function called remove_spaces that gets rid of all the spaces in a given string.
# Hint: Consider replacing a space (" ") with nothing ("").

def remove_spaces(the_string):
  the_string = ""

  return the_string


# Tests:
assert remove_spaces("Jordann Osborn") == "JordannOsborn"
assert remove_spaces("The quick brown fox jumped over the lazy dog.") == "Thequickbrownfoxjumpedoverthelazydog."
assert remove_spaces("A          lot         of            spaces.") == "Alotofspaces."
