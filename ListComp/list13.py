names = ["Barack Obama", "Harry Potter", "Marie Curie"]

firsts = []
for name in names:
    firsts.append(name.split()[0])

print(firsts)

firsts_list = [name.split()[0] for name in names]

print(firsts_list)