def main():
    counts = {}  

    # Infinite loop to continuously prompt the user for input
    while True:
        user_input = input("Enter a number: ") 
        
        # Check if the user pressed Enter without typing anything (empty input)
        if user_input == "":  
            break  

        # Convert the user input into an integer
        num = int(user_input)
        
        # If the number is already in the dictionary, increment its count by 1
        if num in counts:
            counts[num] += 1
        else:  
            counts[num] = 1

    # After collecting all the inputs, loop through the dictionary to display the counts
    for num, count in counts.items():
        # Print the number and how many times it appeared
        print(f"{num} appears {count} times.")

# Check if this script is being run directly, and call the main function
if __name__ == "__main__":
    main()
