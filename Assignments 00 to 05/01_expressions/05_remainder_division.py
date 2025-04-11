def main():
    # Ask the user for the numbers
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))
    
    # Calculate the result and remainder
    result = dividend // divisor
    remainder = dividend % divisor
    
    # Display the result
    print(f"The result of this division is {result} with a remainder of {remainder}")

if __name__ == "__main__":
    main()
