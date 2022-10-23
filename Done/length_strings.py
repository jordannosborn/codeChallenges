# Challenge: Length Strings
# Create a function called length_strings that accepts two strings and returns the length of both of them combined.

def length_strings(string1, string2):
  length_string1 = len(string1)
  length_string2 = len(string2)
  return length_string1 + length_string2


# Tests:
assert length_strings("cat", "dog") == 6
assert length_strings("abcdefghijklmnopqrstuvwxy", "z") == 26
assert length_strings("     ", " ") == 6
