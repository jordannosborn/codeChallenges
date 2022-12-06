# Challenge: Print dictionary keys and values
# Create a function called print_dictionary_keys_and_values that prints both 
# the keys and values of a dictionary, one at a time.
#
# Note that this function requires two print statements. One will print the
# key and then another will prints its value immediately after.


def print_dictionary_keys_and_values(the_dictionary):
  for key, value in the_dictionary.items():
    print(key)
    print(value)


# Tests:

# Assuming a dictionary like this:

# {'name': 'Kevin', 'age': 22, 'number_of_pets': 2}

# The function should print this:

# name
# Kevin
# age
# 22
# number_of_pets
# 2


print_dictionary_keys_and_values({'name': 'Kevin', 'age': 22, 'number_of_pets': 2})
