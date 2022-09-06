# Challenge: Count dudes in array
# Create a function called count_dudes_in_array that counts the number of elements in an array with the value "dude"
# Hint: Consider using a for loop to cycle through each element in an array and check for "dude"
# Hint: You probably need a variable to keep track of the number of "dude" items.

def count_dudes_in_array(the_array):
  return 0


# Tests:
assert count_dudes_in_array(["yo", "dude"]) == 1
assert count_dudes_in_array(["dude", "yo", "dude"]) == 2
assert count_dudes_in_array(["what", "ever"]) == 0