"""
Rewrite the code below as a list comprehension
"""

product_prices = {
    "bread": 0.2, "chocolate": 1,
    "book": 20, "car": 20_000,
}

expensive = []
for product, price in product_prices.items():
    if price > 100:
        expensive.append(product)

print(expensive)

expensive = []
expensive = [product for product, price in product_prices.items() if price > 100]
print(expensive)
