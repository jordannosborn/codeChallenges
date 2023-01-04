# Challenge: Count families with Kevin (fixed)
# Fox the function called count_families_with_kevin that counts the number of
# families that have a Kevin. The previous version didn't into account the
# possibility of two Kevin's in the same family. Now it does.
#
# HINT: You only want to count a family that has Kevin once. So if there are 
# two Kevins in a family you'll want to stop iterating through the family array
# and move on to the next array. 
# Conisder the break keyword: https://www.w3schools.com/python/ref_keyword_break.asp

def count_families_with_kevin(families):
  total = 0
  for family in families:
    for name in family:
      if name == "Kevin":
        total += 1
        break
  return total

# Tests:
assert count_families_with_kevin([['Kevin', 'Jude', 'Amie', 'Jordann'], ['Bob', 'Sara', 'Jane'], ['Doug', 'Kevin', 'Raj']]) == 2
assert count_families_with_kevin([['Kevin', 'Jude', 'Amie', 'Kevin'], ['Bob', 'Sara', 'Jane'], ['Doug', 'Kevin', 'Raj']]) == 2
assert count_families_with_kevin([['Bob', 'Sara', 'Jane'], ['Doug', 'Raj']]) == 0
