# Challenge: Print dictionary keys unless weight
# Create a function called print_dictionary_keys_unless_weight that prints 
# only the keys of a dictionary, one at a time, unless the key is "weight",
# because that's...like...totally embarrassing. 


def print_dictionary_keys_unless_weight(the_dictionary):
  for key, value in the_dictionary.items():
    if key != "weight":
      print (key)



# Test:

# Assuming a dictionary like this:

# {'name': 'Jude', 'weight': 90, 'age': 49, }

# The function should print this:

# name
# age

print_dictionary_keys_unless_weight({'name': 'Jude', 'weight': 90, 'age': 49, })
