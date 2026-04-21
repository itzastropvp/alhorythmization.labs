prices = [100, 200, 300, 400]
discounted_price = list(map(lambda x: x-x*0.15, prices))
print(list(discounted_price))