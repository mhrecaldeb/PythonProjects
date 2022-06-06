numbers = [42, 73, 0, 16, 10]

is_big = []
for num in numbers:
    is_big.append(num > 10)

print(is_big)

is_big_list = [num > 10 for num in numbers]
print(is_big_list)

