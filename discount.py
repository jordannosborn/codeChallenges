# Challenge: Discount
# Create a function called discount that returns a discounted price, but only if the discount is not too much.
# The function should have two parameters:
# 1. The original price
# 2. The amount to be discounted.
# The function should return the amount after the discount. So if the price is 100 and the discount is 20, the function should return 80.
# However, if the discount is higher than the price, simply return the original price. So if the price is 100 and the discount is 150 the function should return 100.

def discount(price, discount):
  total = price - discount
  if discount < price:
    return total
  elif discount > price:
    return price

# Tests:
assert discount(100, 20) == 80
assert discount(200, 10) == 190
assert discount(100, 150) == 100
