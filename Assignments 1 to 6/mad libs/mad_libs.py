def mad_libs():
    # Welcome message to the player with emojis
    print("👋 Welcome to the Mad Libs Game! 🎭🐾")
    print("📝 Please provide the following words to build your wild story! 🌈")
    print("(Let's make a silly story together! 🤪✍️)\n")

    # Giving user a choice to see instructions
    see_instructions = input("📘 Would you like to see the instructions? (yes/no): ").strip().lower()
    if see_instructions == "yes":
        print("\n🔹 You will be asked to enter different kinds of words like nouns, verbs, and adjectives. 🧠")
        print("🔹 These words will be used to fill in a super silly story. 📖")
        print("🔹 Be as creative or goofy as you like — that's the fun of Mad Libs! 😂🎨\n")

    # Taking user inputs for different types of words with emoji prompts
    adjective1 = input("✨ Adjective: ")
    noun1 = input("🐵 Noun: ")
    verb1 = input("🏃 Verb (past tense): ")
    adverb1 = input("🌀 Adverb: ")
    adjective2 = input("🌟 Another Adjective: ")
    noun2 = input("🦁 Another Noun: ")
    noun3 = input("🐘 One More Noun: ")
    verb2 = input("🍦 Another Verb: ")
    adverb2 = input("🚀 One More Adverb: ")

    # Creating a story by inserting the user's inputs into the string
    story = f"""
    🦓🐾 Today I went to the zoo. I saw a(n) {adjective1} {noun1} jumping up and down in its tree 🌳.
    It {verb1} {adverb1} through the large tunnel that led to its {adjective2} {noun2}. 🕳️🏞️
    I got some peanuts 🥜 and passed them through the cage to a gigantic gray {noun3},
    towering above my head. 🐘🤯 Feeding that animal made me hungry. 😋
    I went to get a {verb2} scoop of ice cream. 🍨 It filled my stomach {adverb2}. 🤤
    Afterwards, I had to run to catch our 🚌 — what a wild day! 🌞🎢
    """

    # Displaying the completed Mad Libs story
    print("\n🎉 Here's your Mad Libs story! Ready for a laugh? 😂\n")
    print(story)

    # Ask if the user wants to play again
    play_again = input("🔁 Would you like to create another Mad Libs story? (yes/no): ").strip().lower()
    if play_again == "yes":
        print("\n✨ Let's go again! Bring on the silliness! 🤪✨\n")
        mad_libs()
    else:
        print("\n👋 Thanks for playing Mad Libs! Come back soon for more laughs! 🎊🐒")

# Calling the function to run the game
mad_libs()
