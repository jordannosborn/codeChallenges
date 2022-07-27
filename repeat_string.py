# Challenge: Repeat string
# Create a function called repeat_string that accepts a string and an integer and repeats that string that many times.
# For example, repeat_string("Jordann", 3) should return "JordannJordannJordann"


def repeat_string(the_character, repeat_number):
  string = the_character*repeat_number
  return string


# Tests:
assert repeat_string("Jordann", 3) == "JordannJordannJordann"
assert repeat_string("ab", 4) == "abababab"
assert repeat_string("!", 10) == "!!!!!!!!!!"

