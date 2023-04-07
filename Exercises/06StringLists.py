message = input("Tell me a word: ")

reverse = message[::-1] #reverses the message


if message == reverse:
    print("Your word is a palindrome (reads the same forwards and backwards.)")
else:
    print("Your word is not a palindrome (reads the same forwards and backwards.)")