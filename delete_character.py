# Challenge: Delete a character
# Create a function called delete_character that deletes all occurances of a character in a string.
# Hint: This is very similar to remove_spaces.py, except it's not a space being removed -- it's some other character the user chooses.

def delete_character(the_string, the_character):
  return ""


# Tests:
assert delete_character("Jordann Osborn", "o") == "Jrdann Osbrn"
assert delete_character("Jude the nude crude dude", "u") == "Jde the nde crde dde"
assert delete_character("ABCDEFGHIJKLMNOPQUSTUVWXYZ", "A") == "BCDEFGHIJKLMNOPQUSTUVWXYZ"
