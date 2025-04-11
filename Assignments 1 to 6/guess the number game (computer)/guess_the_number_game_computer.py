import time

def computer_guesses_number():
    # 🎮 Game introduction
    print("""
═══════════════════════════════════════
🧠 Welcome to 'Guess the Number' – Computer Edition! 🤖
═══════════════════════════════════════
🧩 Think of a number between 1️⃣ and 💯 and I'll try to guess it!
📢 Please respond honestly with:
    🔼 'l' = Too low
    🔽 'h' = Too high
    ✅ 'c' = Correct
🧠 Let's see how smart I am! 😎
""")
    input("👋 Press Enter when you're ready... 🎯\n")

    # Initialize game variables
    low = 1
    high = 100
    attempts = 0
    guesses = [] 
    max_attempts = 7  

    # 🌀 Main guessing loop
    while low <= high:
        if attempts >= max_attempts:
            print("⏱️ Uh oh! I've reached my maximum attempts! 😓")
            break

        guess = (low + high) // 2
        guesses.append(guess)
        attempts += 1

        print(f"\n🔍 Attempt #{attempts}: Is your number {guess}? 🤔")
        feedback = input("💬 Enter 🔽 'h', 🔼 'l', or ✅ 'c': ").strip().lower()

        if feedback == 'c':
            print(f"\n🎉 Woohoo! I guessed it right – your number is {guess}! 🎯")
            print(f"🤓 It only took me {attempts} attempts! 🥳")
            break
        elif feedback == 'h':
            high = guess - 1
            print("📉 Got it! I'll guess lower next time! ⬇️")
        elif feedback == 'l':
            low = guess + 1
            print("📈 Alright! I'll guess higher next time! ⬆️")
        else:
            print("❌ Oops! Please respond with 'h', 'l', or 'c'. 😅")

        time.sleep(1)  

    else:
        print("😵 I couldn't guess it... Did you change your number? 🤨")

    # 📜 Show guess history
    print("\n🧾 My guesses were:")
    print(" 👉 ", ' ➡️ '.join(str(g) for g in guesses))
    print("\n👋 Thanks for playing! Come back soon! ✨🎮")

# ▶️ Run the game
computer_guesses_number()
