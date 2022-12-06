# Challenge: print reverse name by calling a function
# This challenge is about calling a function inside a function.
#
# It requires two functions:
#
# 1. reverse_string(the_string), which accepts a string and returns the 
# string reversed. You'll need to create this function yourself.
#
# 2. print_name(name), which calls reverse_string, passing the name to it and
# prints the string reversed.

def reverse_string(the_string):
  return the_string[::-1]


def print_name(name):
  return reverse_string(name)


# Tests:

# First, let's make sure you've made a function called reverse_string that
# returns the reverse of a string.
assert(reverse_string('Jude') == 'eduJ')
assert(reverse_string('Jordann') == 'nnadroJ')

# Now let's see if print_name is calling reverse_string properly. If it is, then
# print_name('Jude') should print this:

# eduJ

print_name('Jude')
