# Challenge: Count Judes
# Create a function called count_judes that accepts and array of families and
# counts the number of people named "Jude".
#
# HINT: Some Families may have more than one "Jude", so this is not about 
# counting the numbe of families with Jude, but rather than total number of 
# Judes in all families.

def count_judes(families):
  total = 0
  for family in families:
    for name in family:
      if name == "Jude":
        total += 1
  return total

# Tests:
assert count_judes(
  [
    ['Kevin', 'Jude', 'Amie', 'Jordann'], 
    ['Jude', 'Bob', 'Sara', 'Jane', 'Jude'], 
    ['Doug', 'Kevin', 'Raj']
  ]
) == 3
assert count_judes([['Bob', 'Sara', 'Jane'], ['Doug', 'Raj']]) == 0
