from random import randint
guess = int(input("Guess a number between 1 and 10: "))
number = randint(1,10)
while(guess != number):
    if (guess > number):
        guess = int(input("Your number was too high, guess again... "))
    else: 
        guess = int(input("Your number was too low, guess again... "))
print(f"You guessed it! The number is {number}")