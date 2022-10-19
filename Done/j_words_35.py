# Challenge: J words
# Create a function called j_words that accepts an array of strings as a parameter and counts the number of 
# items in that array that start with the letter "j"
# Hint: You wil probably need to loop through each item in an array and check that it starts with "j".
def first_is_j(the_string):
 charsToMatch = ('j', 'J')
 return the_string.startswith(charsToMatch)


def j_words(the_array):
 num_j = 0
 for x in the_array:
  if first_is_j(x) is True:
   num_j += 1
 return num_j


# Tests:
assert j_words(["jordann", "jude", "kevin"]) == 2
assert j_words(["kitty", "jude", "kevin"]) == 1
assert j_words(["kitty", "amie", "kevin"]) == 0