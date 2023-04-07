name = input("What's your name? ")
age = input ("What's your age? ")
bday = input("Has your birthday passed? Y/N ")

if bday == "Y":
    hundred = (2023-int(age))+100
    print(f"You'll be 100 years old in {hundred}.")
elif bday == "N":
    hundred = (2023-int(age))+99
    print(f"You'll be 100 years old in {hundred}.")