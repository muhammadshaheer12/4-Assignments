def main():
    # Loop 20 times to generate the first 20 even numbers
    for i in range(20):
        # Multiply the loop index i by 2 to get the corresponding even number
        even_number = i * 2
        
        # Print the even number on the same line, separated by spaces
        print(even_number, end=" ")

# Check if the script is being run directly (i.e., not imported as a module)
if __name__ == "__main__":
    # Call the main function to execute the program
    main()
