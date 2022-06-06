ref_indices = {
    "milk": 1, "butter": 2, "coffee": 3, 
    "water": 4, "tea": 5, "bread": 6,
}

products = ["tea", "bread", "water"]

indices = []
for product in products:
    indices.append(ref_indices[product])

print(indices)

indices_list = [ref_indices[product] for product in products]
print(indices_list)