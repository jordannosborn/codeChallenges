# Challenge: Reverse a string
# Create a function called reverse_string that returns a string that has been
# reversed. So the string "jordann" should be return as "nnadroj".


def reverse_string(the_string):
  return the_string[::-1]


assert reverse_string('jordann') == 'nnadroj'
assert reverse_string('bud') == 'dub'