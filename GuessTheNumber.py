import random
"""
""""""This is a module that generates pseudo-.random values and does som other cool stuffs""""""

print("GUESS THE NUMBER")
GenerateNumber = random.randint(0,3)
GuessedNumber = int(input("Enter a Number (0 - 3): "))

print(f"Computer: {GenerateNumber}")
print(f"Player: {GuessedNumber}")

if GuessedNumber < 0 or GuessedNumber > 3:
    print("Error! \nEnter value from 0 - 3")
elif GenerateNumber == GuessedNumber:
    print ("You Won!")
elif GenerateNumber != GuessedNumber:
    print("You Lose!")

    """

def GuessTheNumber(x):
    GuessTheNumber = random.randint(1,x)
    guess = 0
    trial = 0

    while GuessTheNumber != guess:
        guess = int(input("Enter a number: "))
        trial +=1
        if guess > GuessTheNumber:
            print("Sorry! Too high guess again")
        elif guess < GuessTheNumber:
            print("Sorry! Too low guess again")

    print(f"Congrats! You've guessed the number {guess} correctly on {trial} trial")

    
GuessTheNumber(10)
