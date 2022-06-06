string = " I like pizza."

doubled = []

for char in string:
    doubled.append(2 * char)

print(doubled)


doubled_list = [2 * char for char in string]

print(doubled_list)