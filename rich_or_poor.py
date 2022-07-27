# Challenge: You're poor!
# Create a function called rich_or_poor that accepts the parameters my_money and minimum.
# If my_money is less than minimum return "You're poor!"
# If my_money is the same or more than minimum return "You're rich!"
# However, if my_money is more than twice minimum return "You're ballin!!!"


def rich_or_poor(my_money, minimum):
  if my_money < minimum:
    return "You're poor!"
  elif my_money >= minimum and my_money <= 2*minimum:
    return "You're rich!"
  elif my_money > 2*minimum:
    return "You're ballin!!!"


# Tests:
assert rich_or_poor(9, 10) == "You're poor!"
assert rich_or_poor(11, 10) == "You're rich!"
assert rich_or_poor(21, 10) == "You're ballin!!!"
