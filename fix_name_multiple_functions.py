# Challenge: Fix name with multiple functions
# Write three functions that all work together to fix up a first name
# so that the first name starts with a capital letter and ends with
# the last name, "Osborn".
# You'll need to write three functions:
# 1. add_osborn that adds the last name.
# 2. first_upper that makes sure the first name starts with a capital letter.
# 3. fix_name that ties it all together by calling the previous 2 functions.


def add_osborn(name):
    return ''


def first_upper(name):
    return ''


def fix_name(name):
    return ''

assert fix_name('jude') == 'Jude Osborn'
assert fix_name('amie') == 'Amie Osborn'
assert add_osborn('bob') == 'bob Osborn'
assert first_upper('abc') == 'Abc'