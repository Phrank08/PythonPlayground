import random
def ComputerGuess(x):
    low = 1
    high = x
    feedback = ''
    #guess = 0

    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = high

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (c)???").lower()

        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1

    print(f"Hoo-ray! I've guessed number {guess} correctly")

ComputerGuess(100)
