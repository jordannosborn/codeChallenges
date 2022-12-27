# Challenge: Has kitty in challenge
# Create a function called has_kitty_in_challenge that accepts an array of
# challenge filenames and returns true of any of them have the word "kitty" in
# them.
#
# HINT: As soon as "kitty" is found you can return True. No need to cycle through
# all the other elements in the array.


def has_kitty_in_challenge(challenges):
  for x in challenges:
    split = x.split("_")
    if "kitty" in split:
      return True
  return False

# Tests:
assert has_kitty_in_challenge(['make_stuff_10', 'has_kitty_15', 'print_all_kevins_10']) == True
assert has_kitty_in_challenge(['divisible_by_ten_20', 'count_dudes_5', 'print_except_jude_25']) == False
