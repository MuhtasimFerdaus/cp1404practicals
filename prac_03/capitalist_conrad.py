import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "stock_prices.txt"

out_file = open(FILENAME, 'w')

price = INITIAL_PRICE
day = 0
print(f"Starting price: ${price:.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    day += 1
    if random.randint(1, 2) == 1:
        price *= (1 + random.uniform(0, MAX_INCREASE))
    else:
        price *= (1 - random.uniform(0, MAX_DECREASE))

    print(f"On day {day} price is: ${price:.2f}", file=out_file)

out_file.close()