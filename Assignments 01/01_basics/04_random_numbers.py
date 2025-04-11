import random  

# Define the main function
def main():
    # Print an introductory message
    print("Here are 10 random numbers between 1 and 100:")

    # Loop 10 times to generate 10 random numbers
    for _ in range(10):
        # Generate a random integer between 1 and 100 (inclusive)
        number = random.randint(1, 100)

        # Print the number on the same line with a space after it
        print(number, end=' ')  

    # Print a newline character after all 10 numbers are printed
    print()  

# This line checks if the script is being run directly
# If so, it calls the main function to start the program
if __name__ == "__main__":
    main()
