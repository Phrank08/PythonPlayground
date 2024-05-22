import random  

words = ['python', 'ruby', 'kotlin', 'JavaScript', 'swift', 'java']     # List of words that can be chosen for the game

chosenWord = random.choice(words)       # Randomly choose one word from the list 'words' and assign it to 'chosenWord'

word_display = ['_' for _ in chosenWord]        # Create a list of underscores with the same length as the chosen word

attempts = 8        # Set the number of allowed incorrect attempts

print("Welcome to HANGMAN")     

"""
Start the main game loop, which continues until no attempts remain or the word is guessed
"""
while attempts > 0 and '_' in word_display:
    
    print("\n" + ' '.join(word_display))    # Print the current state of the guessed word, separated by spaces

    guess = input("Guess a letter: ").lower()
    
    # Check if the guessed letter is in the chosen word
    if guess in chosenWord:
        for index, letter in enumerate(chosenWord):
            """
            If the guessed letter is in the word, iterate through each letter in 'chosenWord
              """
            if letter == guess:
                word_display[index] = guess # reveal letter
    else:
        print("The letter doesn't appear in the word")
        attempts -= 1

"""
Game Conclusion: Check if the player has successfully guessed the word or run out of attempts
"""
if '_' not in word_display:
    # If there are no underscores left in 'word_display', the player has guessed the word
    print("You guessed the word!")
    print(' '.join(word_display))
    print('You survived')
else:
    # If there are still underscores left, the player has run out of attempts
    print("You ran out of attempts. The word was: " + chosenWord)
    print('You lost')
