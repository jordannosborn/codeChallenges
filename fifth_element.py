# Challenge: Fifth element
# Create a function called fifth_element that returns only the value of the fifth element of an array.
# So if an array has five elements, it should return the last one. Or if it has six it should return the second to last.
# If the array has less than five elements you should return "".
# Hint: Don't forget that arrays are "zero indexed" that means they start with 0, not 1.


def fifth_element(the_array):
  if len(the_array) >= 5:
    fifth = the_array[4]
    return fifth
  else:
    return ""

# Tests:
assert fifth_element(["a", "b", "c", "d", "e"]) == "e"
assert fifth_element(["Jude", "Amie", "Kevin", "Ana", "Jordann", "Kitty", "Charles", "Pickles"]) == "Jordann"
assert fifth_element(["a"]) == ""
assert fifth_element(["a", "b"]) == ""
