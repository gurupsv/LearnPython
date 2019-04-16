import itertools

for x in itertools.count(50, 5):
    print(x)
    if x == 80:
        break

x=0
for c in itertools.cycle("RACECAR"):
    print(c)
    x += 1
    if x > 50:
        break

for r in itertools.repeat(True):
    print(r)
    x += 1
    if x > 60:
        break

# Permutations:
election={1:"Barb", 2:"Karen", 3:"Erin"}
for p in itertools.permutations(election.values()):
    print(p)

# Combinations
colorsForPainting=["Red","Blue","Purple","Orange","Yellow"]
for c in itertools.combinations(colorsForPainting,3):
    print(c)
