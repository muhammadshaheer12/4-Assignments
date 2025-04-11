def print_multiple(message, repeats):
    # Loop through the range of repeats and print the message each time
    for _ in range(repeats):
        print(message)

def main():
    # Prompt the user for the message and the number of repeats
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    
    # Call the function to print the message the specified number of times
    print_multiple(message, repeats)

if __name__ == "__main__":
    main()  
