firsts = []
for word in "The quick brown for jumps.".split():
    firsts.append(word[0])

print(firsts)

first_list = [word[0] for word in "The quick brown for jumps.".split()]

print(first_list)
