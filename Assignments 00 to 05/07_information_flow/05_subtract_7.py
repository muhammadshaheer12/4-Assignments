# Helper function to subtract 7 from the number
def subtract_seven(num):
    return num - 7

# Main function
def main():
    # Ask the user to input a number
    num = int(input("Enter a number: "))
    
    # Call the subtract_seven function and store the result
    result = subtract_seven(num)
    
    # Print the result
    print(f"The result after subtracting 7 is: {result}")

# Run the main function if this script is being executed
if __name__ == "__main__":
    main()
