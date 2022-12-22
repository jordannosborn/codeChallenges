# Challenge: Total challenge allowance.
# Create a function called total_challenge_allowance that accepts an array of
# challenge filenames, extracts the allowance reward and adds them all together
# to return the total.
#
# Hint: Consider split()

def total_challenge_allowance(challenges):
  total = 0
  for x in challenges:
    split = x.split("_")
    last_element = split[-1]
    total += int(last_element)
  return total

# Tests:
assert total_challenge_allowance(['make_stuff_10', 'has_kitty_15', 'print_all_kevins_10']) == 35
assert total_challenge_allowance(['divisible_by_ten_20', 'count_dudes_5', 'print_except_jude_25']) == 50
