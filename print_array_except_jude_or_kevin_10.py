# Challenge: Print array except "Jude" or "Kevin"
# Create a function called print_girls that prints each element of 
# an array, unless that element is either "Jude" or "Kevin", in which case 
# nothing is printed.


def print_array_except_jude_or_kevin(the_array):
  for x in the_array:
    if x != "Jude" and x != "Kevin":
      print(x)

    

# Assuming an array like this:

# ["Jordann", "Jude", "Kevin"]

# The function should print this:

# Amie
# Jordann

print_array_except_jude_or_kevin(["Amie", "Jude", "Jordann", "Kevin"])