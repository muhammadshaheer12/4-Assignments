import random
import time

# Function to start the Hangman game
def hangman():
    # List of possible words categorized by themes
    word_categories = {
        "programming": ['python', 'java', 'html', 'css', 'javascript', 'developer', 'algorithm'],
        "animals": ['elephant', 'giraffe', 'kangaroo', 'panda', 'tiger', 'zebra'],
        "sports": ['soccer', 'basketball', 'baseball', 'cricket', 'tennis', 'hockey']
    }
    
    # Difficulty levels (easy: short words, medium: medium words, hard: long words)
    difficulty_levels = {'easy': 4, 'medium': 6, 'hard': 8}
    
    # Ask player to select difficulty level
    print("""
🎮✨ Welcome to Hangman! ✨🎮
Can you guess the word? 🤔
You have 6 chances to guess the word correctly. Let's get started! 🍀
""")
    
    # Prompting player to choose difficulty level
    print("🌟 Select Difficulty Level: 🌟")
    print("1. Easy (short words) 🌱")
    print("2. Medium (medium words) 🏅")
    print("3. Hard (long words) 🏆")
    
    # Capture player's choice and set max word length based on difficulty
    difficulty_choice = input("🔢 Enter the number (1/2/3): ")
    
    if difficulty_choice == '1':
        max_word_length = difficulty_levels['easy']
    elif difficulty_choice == '2':
        max_word_length = difficulty_levels['medium']
    elif difficulty_choice == '3':
        max_word_length = difficulty_levels['hard']
    else:
        # Default to medium if invalid input
        print("🚨 Invalid choice, defaulting to Medium level. 🚨")
        max_word_length = difficulty_levels['medium']
    
    # Ask player to select a word category
    print("🌍 Select a word category: 🌍")
    print("1. Programming 🖥️")
    print("2. Animals 🦁")
    print("3. Sports 🏀")
    
    category_choice = input("🔢 Enter the number (1/2/3): ")
    
    if category_choice == '1':
        category = "programming"
    elif category_choice == '2':
        category = "animals"
    elif category_choice == '3':
        category = "sports"
    else:
        # Default to programming category if invalid input
        print("🚨 Invalid choice, defaulting to Programming. 🚨")
        category = "programming"
    
    # Get words from selected category and filter based on difficulty
    word_list = word_categories[category]
    filtered_words = [word for word in word_list if len(word) <= max_word_length]
    
    # Randomly select a word from the filtered list
    word_to_guess = random.choice(filtered_words)
    
    # Create a list to store correctly guessed letters or underscores for hidden letters
    guessed_letters = ['_'] * len(word_to_guess)
    
    # Set the maximum number of incorrect guesses allowed (6 chances)
    max_attempts = 6
    wrong_guesses = 0
    
    # List to track the wrong letters that have been guessed
    wrong_guessed_letters = []
    
    # Timer and score tracking
    start_time = time.time()
    
    # Main game loop (continues as long as wrong_guesses < max_attempts)
    while wrong_guesses < max_attempts:
        # Display the current state of the word (with underscores for unguessed letters)
        print(f"\n🔠 Current word: {' '.join(guessed_letters)}")

        # Display the wrong guesses made so far
        if wrong_guesses > 0:
            print(f"💔 Wrong guesses: {', '.join(wrong_guessed_letters)}")
        
        # Show the player how many attempts they have left
        print(f"⏳ You have {max_attempts - wrong_guesses} attempts left. ⏳")
        
        # Display Hangman figure based on the number of wrong guesses
        hangman_stages = [
            '''
             -----
             |   |
                 |
                 |
                 |
                 |
            =========
            ''',
            '''
             -----
             |   |
             O   |
                 |
                 |
                 |
            =========
            ''',
            '''
             -----
             |   |
             O   |
             |   |
                 |
                 |
            =========
            ''',
            '''
             -----
             |   |
             O   |
            /|   |
                 |
                 |
            =========
            ''',
            '''
             -----
             |   |
             O   |
            /|\\  |
                 |
                 |
            =========
            ''',
            '''
             -----
             |   |
             O   |
            /|\\  |
            /    |
                 |
            =========
            ''',
            '''
             -----
             |   |
             O   |
            /|\\  |
            / \\  |
            =========
            '''
        ]
        print(hangman_stages[wrong_guesses]) 
        
        # Prompt the player to enter a guess (a letter)
        guess = input("🔍 Enter a letter: ").lower()

        # Validate the guess: Ensure it is a single alphabetic character
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a valid letter. Try again! ⬇️")
            continue
        
        # If the letter has already been guessed (either correctly or incorrectly)
        if guess in guessed_letters or guess in wrong_guessed_letters:
            print(f"❌ You've already guessed '{guess}'. Try another letter. 🔄")
            continue
        
        # Check if the guessed letter is in the word
        if guess in word_to_guess:
            print(f"✅ Good guess! '{guess}' is in the word. 🎉")
            # Update the guessed letters list with the correct guess
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_letters[i] = guess
        else:
            # If the guess is incorrect, increment wrong_guesses and add to the wrong guessed letters list
            print(f"❌ Sorry, '{guess}' is not in the word. 😞")
            wrong_guesses += 1
            wrong_guessed_letters.append(guess)
        
        # Check if the player has guessed all letters correctly
        if "_" not in guessed_letters:
            print(f"\n🎉 Congratulations! You've guessed the word: {''.join(guessed_letters)} 🎊")
            break
    else:
        # If the player runs out of attempts, the game ends with a loss
        print(f"\n😞 Game Over! You've run out of attempts. The word was: {word_to_guess}.")
        print("Better luck next time! 🍀")
    
    # Calculate the time taken for the game
    time_taken = time.time() - start_time
    print(f"⏱ Time taken: {round(time_taken, 2)} seconds ⏱")
    
    # Ask if the player wants to play again
    replay = input("\n🎮 Would you like to play again? (yes/no): ").lower()
    if replay == "yes":
        print("🎉 Let's go again! 🔁")
        hangman()
    else:
        print(f"🎉 Thanks for playing! Hope you had fun! 🎮💫")
        
# Start the game
hangman()
