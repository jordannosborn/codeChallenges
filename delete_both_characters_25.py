# Challenge: Delete both characters.
# Create a function called delete_both_characters that deletes two characters from a string.
# The first parameter is the string, the second and third are the characters to delete.
# HINT: Refer to the previous challenge called "delete_character".


def delete_both_characters(the_string, first_character, second_character):
  x = the_string.replace(first_character, "").replace(second_character, "")
  return x


# Tests:
assert delete_both_characters("Jordann Osborn", "o", "n") == "Jrda Osbr"
