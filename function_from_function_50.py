# Challenge: Function from function
# Create a function that calls other functions.
# 1. Create a function called years_to_days that accepts the parameters "years" and returns the number of days.
# 2. Create another function called name_and_years that accepts a name and years and returns a string that says "<name of person> has lived <number of years>."
# For example: "Jude has lived 17885 days."
# The name_and_years function should call the years_to_days function, passing it the years.
# Hint: Here's a discussion on how to call a function from a function: https://stackoverflow.com/questions/32958704/how-do-you-call-a-function-in-a-function
# Hint: You will need to convert the years parameter to a string in name_and_years.
# Hint: There are 365 days in a year.

def years_to_days(years):
  return 0


def name_and_years(name, years):
  return ""


# Tests:
assert name_and_years("Jude", 49) == "Jude has lived 17885 days."
assert name_and_years("Jordann", 15) == "Jordann has lived 5475 days."