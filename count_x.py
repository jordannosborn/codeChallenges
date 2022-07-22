# Challenge: Count the letter x
# Create a function called count_x that returns the number of lower case "x" chracters in a string.
# Hint: You probably need to use a for loop to cycle through each character in the string and check if it's an x.
# Hint: Use a separate varable to keep track of the number of occurances of "x".

def count_x(the_string):
  x = the_string.count('x')
  return x

# Tests -- don't delete anything below this line!
assert count_x("xyz") == 1
assert count_x("xyzx") == 2
assert count_x("yz") == 0
assert count_x("xxxxxxxxxx") == 10
