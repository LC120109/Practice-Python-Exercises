import sys
message = input("Tell me a number: ")

number = int(message)

lists = []

for i in range(1, number+1): #doesn't skip the number itself
    if int(message) % i == 0:
        lists.append(i)
    else:
        continue

print(lists)