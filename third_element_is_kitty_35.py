# Challenge: Third element is kitty
# Create a function called third_element_is_kitty that returns true if the third element of an array is the string "kitty", and false if it's not.
# The function should ignore case. So "Kitty", "kitty" and "KITTY" should all return true.
# The function should check if the array is at least 3 elements, and if not return true.
# Hint: Refer to the previous challenge, fifth_element.py
# Hint: You might want to convert the string to lower case before checking if it's "kitty"
# Hint: Don't forget that arrays are "zero" indexed, which means they start with 0, not 1.

def third_element_is_kitty(the_array):
    if len(the_array) >= 3:
        the_array_lower = the_array[2].lower()
        if the_array_lower == "kitty":
            return True
        else:
            return False
    else:
        return False

# Tests:
assert third_element_is_kitty(["Charles", "Pickles", "Kitty"]) == True
assert third_element_is_kitty(["Charles", "Pickles", "KITTY"]) == True
assert third_element_is_kitty(["Charles", "Pickles", "kitty"]) == True
assert third_element_is_kitty(["Charles", "KITTY", "Pickles"]) == False
assert third_element_is_kitty(["KITTY"]) == False
