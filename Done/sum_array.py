# Challenge: Sum Array
# Create a function called sum_array that sums all the values of an array of integers.

def sum_array(the_array):
  sum = 0
  for i in the_array:
    sum = sum + i
  return sum


# Tests -- don't delete anything below this line!
assert sum_array([1, 1]) == 2
assert sum_array([1, 2, 3, 4]) == 10
assert sum_array([10, 100, 50]) == 160

