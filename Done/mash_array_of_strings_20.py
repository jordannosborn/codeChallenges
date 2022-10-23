# Challenge: Mash array of strings
# Create a function called mash_array_of_strings that accepts an array of strings and
# returns them all mashed into one log string.


def mash_array_of_strings(the_array):
  output = ""
  for x in the_array:
    output += x
  return output


assert mash_array_of_strings(["Leela", "Fry", "Farnsworth"]) == "LeelaFryFarnsworth"
assert mash_array_of_strings(["Zoid", "berg"]) == "Zoidberg"