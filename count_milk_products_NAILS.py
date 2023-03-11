# Challenge: The price of milk
# Create a function called the_price_of_milk that accepts a dictionary 
# of food and another dictionary of toiletries, and returns the combined price 
# of all items that have "milk" in their name.
#
# HINT: The prices are integers so you don't need to worry about decimal points 
# and currency conversion.


def the_price_of_milk(food, toiletries):
    food_total = 0
    toiletries_total = 0
    total = 0
    for key, value in food.items():
        if "milk" in key:
            food_total += value
    for key, value in toiletries.items():
        if "milk" in key:
            toiletries_total += value
    total = toiletries_total + food_total
    return total


# Tests:
assert the_price_of_milk({'eggs': 5, 'milk': 2}, {'shampoo': 6, 'toothbrush': 2}) == 2
assert the_price_of_milk({'butter-milk-bread': 2, 'milk-chocolate': 3, 'peanut-butter': 4}, {'conditioner': 5, 'body-milk-moisterizer': 20}) == 25
