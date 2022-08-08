# Challenge: Sum Arrays
# Create a function called sum_arrays that sums two arrays, then adds them together to return the sum of them both.
# Hint: Refer to previous challenge, sum_array.

def sum_arrays(first_array, second_array):
  sum = 0
  for i in first_array:
    sum = sum + i

  sum1 = 0
  for i in first_array:
    sum1 = sum1 + i

  return sum + sum1

# Tests:
assert sum_arrays([1, 1], [1, 1]) == 4
assert sum_arrays([1, 1], [2, 2]) == 6
