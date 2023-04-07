import sys
while True:
    message = input("Tell me a number (or quit): ")
    if message == "quit" or message == "Quit":
        sys.exit() #to get out of the loop
    elif int(message) % 2 == 0:
        print(f"{message} is even.")
    elif int(message) % 2 != 0:
        print(f"{message} is odd.")
    elif message != int: #in case the input is not a number
        print("Tell me a number, not something else!")
     