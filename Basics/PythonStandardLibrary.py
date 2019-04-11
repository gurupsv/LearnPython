import math
import random

firstName="Guruprasad"
print(len(firstName))
firstName.__len__()

myList=[1,4,55,22,3,67,83]
print(myList.__len__())
print(range(0,10))
print(min(3,4,5,6,-1,2))
print(round(9.9999))
print(abs(-5))
print(pow(2,3))

print(sorted("Guruprasad Shringeri Vidyaranyapura", key=str.upper))
print(sorted(["Guru", "Chandu", "Sudhanva", "Anand"], key=str.upper))

# Factorial and Square Root
print(math.factorial(3))
print(math.sqrt(17))

# Greatest Common Denominator GCD
print(math.gcd(78,98))


# Radmom Numbers
print(random.random())
decider = random.randrange(6)
print(decider)

# Random Choices
lotteryWinners = random.sample(range(100), 5)
print(lotteryWinners)

possiblePets = ["cat", "dog", "fish", "cow"]
print(random.choice(possiblePets))

cards = ["Jack", "Queen", "King", "Ace"]
random.shuffle(cards)
print(cards)