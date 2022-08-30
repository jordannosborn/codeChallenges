# Challenge: Sum Array
# Create a function called sum_array_and_multiply that sums all the values of 
# an array of integers and then multiplies the sum by the parameter "mult".

def sum_array_and_multiply(the_array, mult):
  result = sum(the_array)
  return result * mult


# Tests -- don't delete anything below this line!
assert sum_array_and_multiply([1, 1], 2) == 4
assert sum_array_and_multiply([1, 2, 3, 4], 5) == 50
