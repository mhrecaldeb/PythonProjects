food = ["carrots", "eggs"]
prep = ["raw", "stewed", "boiled"]

combos = [(p, f) for p in prep if p != "stewed" for f in food]
print(combos)

combos2 = [(p, f) for f in food for p in prep if p != "stewed"]
print(combos2)

combos3 = [(p, f) for p in prep for f in food if f != "eggs"]
print(combos3)
