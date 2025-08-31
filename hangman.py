import random
def hangman():

    # Step 1 : Words list 
    words  = ["apple","tiger","house","train","water"]

    #step 2: Random word select
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman Game")
    print("Guess the word, letter by letter!")
    print("Word:","".join(guessed))

    #Step 3 Game loop 
    while attempts  > 0 and "_" in guessed:
        guess = input("\nEnter a letters:").lower()

        # Check already guessed 
        if guess in guessed_letters:
            print("You already guessed this letters.")
            continue
        guessed_letters.append(guess)

        # Check correct guess
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            print("Correct guess!")
        else:
            attempts -= 1
            print(f"Wrong guess | Attempts left: {attempts}")
            print("Word:","".join(guessed))

        # Step 4: Game result 
        if "_" not in guessed:
            print("\nCongratulations! You guessed the word:", word)
        else:
            print("\nGame Over ! The word was:", word)

# Run the game 
hangman()


