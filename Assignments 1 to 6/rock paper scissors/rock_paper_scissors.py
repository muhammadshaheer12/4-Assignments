import random

# Function to play the Rock, Paper, Scissors game
def rock_paper_scissors():
    # Stylized welcome messages with emojis
    print("""
╔══════════════════════════════════════╗
║  Welcome to Rock, Paper, Scissors!   ║
║             👊✋✌                   ║            
╚══════════════════════════════════════╝
    """)

    # Available choices and corresponding emojis
    choices = ["rock", "paper", "scissors"]
    emoji_map = {
        "rock": "👊",
        "paper": "✋",
        "scissors": "✌"
    }

    # Track scores
    player_score = 0
    computer_score = 0
    rounds_played = 0

    # Main game loop
    while True:
        # Prompt user for their choice
        player = input("👉 Choose rock, paper, or scissors (or type 'quit' to exit): ").strip().lower()

        # Option to exit the game
        if player == "quit":
            print("👋 Thanks for playing! Here are the final scores:")
            print(f"🎯 You: {player_score} | 🤖 Computer: {computer_score} | 🧾 Rounds: {rounds_played}")
            break

        # Handle invalid input
        if player not in choices:
            print("❌ Invalid choice! Please type rock, paper, or scissors. 🔁")
            continue

        # Randomly choose for the computer
        computer = random.choice(choices)
        rounds_played += 1

        # Display both choices with emojis
        print("\n🔍 You chose:", f"{player.upper()} {emoji_map[player]}")
        print("🧠 Computer chose:", f"{computer.upper()} {emoji_map[computer]}")

        # Result logic with stylish output
        if player == computer:
            print("🤝 It's a tie! Try again!\n")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("🏆 YOU WIN! 🎊 You're on fire! 🔥\n")
            player_score += 1
        else:
            print("💻 COMPUTER WINS! Better luck next time! 🕹️\n")
            computer_score += 1

        # Display current score
        print(f"📊 Score: You {player_score} - {computer_score} Computer (Round {rounds_played})\n")

# Start the game
rock_paper_scissors()
