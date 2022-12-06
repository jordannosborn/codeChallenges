# Challenge: Print array except parents
# Create a function called print_array_except_parents that prints each element
# of an array, unless that element is either "Dad" or "Mum", in which case 
# nothing is printed.


def print_array_except_parents(the_array):
  for x in the_array:
    if x == "Jordann" or x == "Kevin":
      print(x)



# Assuming an array like this:
#
# ["Jordann", "Dad", "Kevin", "Mum"]
#
# The function should print this:
#
# Jordann
# Kevin

print_array_except_parents(["Jordann", "Dad", "Kevin", "Mum"])

