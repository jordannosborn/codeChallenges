# Challenge: Print array adding 1 to even, 2 to odd
# Create a function called convert_array_usd_to_aud that accepts an array of 
# prices US Dollars to Australian Dollars. Assume the exchange rate is 1.50
# AUD to USD.


def convert_array_usd_to_aud(the_array):
  output = []
  for x in the_array:
    output.append(x * 1.50)
  return output
    

assert convert_array_usd_to_aud([1.00, 2.50, 50.00]) == [1.50, 3.75, 75.00]
