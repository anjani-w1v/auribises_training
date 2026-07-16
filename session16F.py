product_prices = [100,300, 450, 520, 800]
discounted_prices = []

discount = lambda price, percentage : price*percentage
for price in product_prices:
    discounted_prices.append(discount(price,0.50))

print('product_prices:', product_prices)
print('discounted_prices:', discounted_prices)
print('discount:', discount)