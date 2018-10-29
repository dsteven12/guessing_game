from random import randint
guess = None
number = randint(1,10)

while True:
    guess = int(input("Pick a number from 1 to 10: "))
    if (guess < number):
        print("Too low!")
    elif(guess > number):
        print("Too high!")
    else:
        print("You won!!!")
        print(number)
        play_again = input("Do you want to play again? (y/n) ")
        if (play_again == "y"):
            number = randint(1,10)
            guess = None
        else: 
            print("Thank you for playing!")
            break

