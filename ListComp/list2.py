numbers = []
for idx in range(10):
    numbers.append(1 + idx ** 2)

print(numbers)

numbers_list = [1 + idx ** 2 for idx in range(10)]

print(numbers_list)