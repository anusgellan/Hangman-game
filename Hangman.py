import random

def hangman():
    # List of words to choose from
    word_list = ["python", "hangman", "programming", "openai", "computer"]
    # Randomly select a word
    word = random.choice(word_list)
    # Create a list to store the guessed letters
    guessed_word = ["_"] * len(word)
    # Set the number of allowed incorrect guesses
    allowed_incorrect_guesses = 6
    incorrect_guesses = 0
    guessed_letters = []

    print("Welcome to Hangman!")
    print("You have", allowed_incorrect_guesses, "incorrect guesses allowed.")
    print(" ".join(guessed_word))

    while incorrect_guesses < allowed_incorrect_guesses and "_" in guessed_word:
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            print("Good guess!")
            guessed_letters.append(guess)
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print("Incorrect guess.")
            guessed_letters.append(guess)
            incorrect_guesses += 1
        
        print(" ".join(guessed_word))
        print("Incorrect guesses left:", allowed_incorrect_guesses - incorrect_guesses)

    if "_" not in guessed_word:
        print("Congratulations! You've guessed the word:", word)
    else:
        print("You've run out of guesses. The word was:", word)

# Start the game
hangman()
