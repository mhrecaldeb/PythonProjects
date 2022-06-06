values = []
for num in range(10, 23, 2):
    values.append(num % 13)

print(values)

values_list = [num % 13 for num in range(10, 23, 2)]
print(values_list)