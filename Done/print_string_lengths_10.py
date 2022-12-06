# Challenge: Print string lengths
# Create a function called print_string_lengths that prints the length of each
# string in an array


def print_string_lengths(the_array):
  for x in the_array:
    print(len(x))



# Assuming an array like this:

# ['abc', 'a', 'abcdefg']

# The function should print this:

# 3
# 1
# 7


print_string_lengths(['abc', 'a', 'abcdefg'])
