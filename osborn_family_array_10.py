# Challenge: Osborn family array
# Create a function called osborn_family_array that returns an array of the first name of everyone in the Osborn family.
# If the parameter oldest_to_youngest is True the list should be oldest to youngest.
# If not, it should be youngest to oldest.


def osborn_family_array(oldest_to_youngest):
  return []


# Tests:
assert osborn_family_array(True) == ["Jude", "Amie", "Kevin", "Jordann", "Kitty"]
assert osborn_family_array(False) == ["Kitty", "Jordann", "Kevin", "Amie", "Jude"]
