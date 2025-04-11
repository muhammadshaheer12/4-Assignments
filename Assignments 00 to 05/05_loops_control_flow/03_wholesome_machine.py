def main():
    # Define the correct affirmation
    affirmation = "I am capable of doing anything I put my mind to."
    
    # Start an infinite loop to repeatedly ask the user for input
    while True:
        # Prompt the user to type the affirmation
        user_input = input("Please type the following affirmation: ")
        
        # Check if the user input matches the predefined affirmation
        if user_input == affirmation:
            # If correct, print a success message and break the loop
            print("That's right! :)")
            break  
        else:
            # If incorrect, ask the user to try again
            print("Hmmm That was not the affirmation. Please try again.")

# Ensure the main function is called when the script is executed
if __name__ == "__main__":
    main()
