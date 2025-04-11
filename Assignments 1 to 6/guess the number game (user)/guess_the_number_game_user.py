import random
import time

# Main function to start the game
def guess_the_number_game():
    # 🎮 Game introduction with enhanced emojis and styling
    print("""
🌟✨🎯 Welcome to 'Guess the Number'! 🎉✨🌟
════════════════════════════════════════════
🤖 I'm thinking of a number between 1️⃣ and 💯... 🤔
Can you guess it? You have 🔟 chances! 🧠🕹️
Let's test your intuition and luck! 🍀🔍
════════════════════════════════════════════
""")

    # Generate a random number between 1 and 100
    number = random.randint(1, 100)  
    attempts = 0  
    max_attempts = 10  
    guess_history = []  

    start_time = time.time()  

    # Main guessing loop: continues until the player wins or runs out of attempts
    while attempts < max_attempts:
        try:
            # User input with emoji prompt
            guess = int(input("\n🧙‍♂️✨ Enter your magic number (1-100): "))  
        except ValueError:
            print("🚫 That's not a number! Please enter digits only. 🔢")
            continue

        # Count each guess
        attempts += 1
        guess_history.append(guess)  

        # Evaluate the guess and provide feedback
        if guess < number:
            print("📉 Oops! Too low. Aim higher! 🔼💭")
        elif guess > number:
            print("📈 Whoa! Too high. Try something lower! 🔽🤔")
        else:
            elapsed_time = round(time.time() - start_time, 2)
            print(f"🎊 Woohoo! You nailed it! The number was {number}! 🎯💥")
            print(f"🔢 It took you {attempts} attempt{'s' if attempts > 1 else ''} and {elapsed_time} seconds! ⏱️🥇")
            print(f"📜 Your guesses were: {guess_history} 📝🧾")
            break

        # Remaining guesses feedback
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"⏳ You have {remaining} attempt{'s' if remaining > 1 else ''} left. Keep it up! 🚀💡")
        else:
            elapsed_time = round(time.time() - start_time, 2)
            print(f"💔 Game Over! You've used all your chances. The number was {number}. 😭👎")
            print(f"⏱️ Time spent: {elapsed_time} seconds 🕰️")
            print(f"📜 Your guesses were: {guess_history} 🗒️🧾")

    # Replay prompt
    again = input("🔁 Want to challenge your fate again? (yes/no): 🌀").strip().lower()
    if again == "yes":
        print("\n🎮 Loading new game... 🔄🔮\n")
        guess_the_number_game()
    else:
        print("👋 Thanks for playing! Hope to see you soon! 🌟👑✨")

# 🚀 Launch the game
guess_the_number_game()
