def main():
    # Initialize an empty list to store the user inputs
    values = []
    
    # Start an infinite loop that will keep asking for user input
    while True:
        # Prompt the user to enter a value
        value = input("Enter a value: ")
        
        # If the input is an empty string (the user presses Enter without typing anything),
        # break the loop and stop collecting values
        if value == "":
            break
        
        # Append the entered value to the list
        values.append(value)
    
    # After the loop finishes (when the user presses Enter without typing anything),
    # print out the entire list of collected values
    print("Here's the list:", values)

# Check if this file is being executed directly (not being imported as a module),
# and if so, call the main function to start the program
if __name__ == "__main__":
    main()
