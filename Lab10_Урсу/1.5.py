prices = [100, 200, 300, 400]

discounted_prices = list(map(lambda x: round(x * 0.85, 2), prices))

print(discounted_prices)