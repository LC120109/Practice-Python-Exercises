import random, sys

print("Guessing Game!")
rand_number = random.randint(1, 9)
n_guesses = 0


while n_guesses < 3:
    guess = int(input("Guess my number (between 1, 9) or quit: "))
    if guess == rand_number:
        print("That's it!")
        break
    elif guess < rand_number:
        print("That's too low try again!")
        n_guesses += 1
    elif guess > rand_number:
        print("That's too high, try again.")
        n_guesses += 1   
    
if guess == rand_number:
    print(f"You did it. My number was {rand_number}.")
elif guess != rand_number:
    print(f"You failed. My number was {rand_number}.")