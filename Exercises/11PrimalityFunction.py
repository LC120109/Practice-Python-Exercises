import math, sys

while True:
    message = input("Tell me a number or quit: ")

    if message == "quit" or message == "Quit":
        sys.exit()

    is_prime = False

    n_message = int(message)


    if n_message > 1:
        for i in range(2, int(math.sqrt(n_message))+1): #doesn't skip the number itself
            if n_message % i == 0:
                is_prime = True
                break

    if n_message == 1:
        print(f"{n_message} is not prime.")
    elif is_prime == False:
        print(f"{n_message} is prime.")
    elif is_prime == True:
        print(f"{n_message} is not prime.")

    

