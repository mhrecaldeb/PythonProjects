names = ["Barack Obama", "Harry Potter", "Marie Curie"]
lengths = []
for name in names:
    lengths.append(len(name))

print(lengths)

lengths_list = [len(name) for name in names]
print(lengths_list)
