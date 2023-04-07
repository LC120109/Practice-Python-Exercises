import random

a = []
b = []

lists = []

#generating random list length
randomNumber = random.randint(1, 20)

#generating random number list
for g in range(0, randomNumber):
    n = random.randint(1, 100)
    a.append(n)

randomNumber2 = random.randint(1, 20)

for h in range(0, randomNumber2):
    n = random.randint(1, 100)
    b.append(n)

newA = [*set(a)]
newB = [*set(b)]

for i in newA:
    for y in newB:
        if i == y:
            lists.append(i)
        else:
            continue

print(lists)
