# import sales.calc_prices
# from sales import calc_prices
from sales.calc_prices import increase_price, decrease_price
import sales.format.price as format_price

some_price = 49.90
inc_price = increase_price(value=some_price, percentage=15, formated=True)
print(inc_price)

dec_price = decrease_price(some_price, 15, True)
print(dec_price)

print(format_price.real(50))
