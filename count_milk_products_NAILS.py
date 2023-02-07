# Challenge: The price of milk
# Create a function called the_price_of_milk that accepts a dictionary 
# of food and another dictionary of toiletries, and returns the combined price 
# of all items that have "milk" in their name.
#
# HINT: The prices are integers so you don't need to worry about decimal points 
# and currency conversion.


def the_price_of_milk(food, toiletries):
    return 0


# Tests:
assert the_price_of_milk({'eggs': 5, 'milk': 2}, {'shampoo': 6, 'toothbrush': 2}) == 2
assert the_price_of_milk({'butter-milk-bread': 2, 'milk-chocolate': 3, 'peanut-butter': 4}, {'conditioner': 5, 'body-milk-moisterizer': 20}) == 25
