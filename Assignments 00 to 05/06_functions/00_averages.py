def calculate_average(num1, num2):
    # This function calculates the average of two numbers.
    # It adds the two numbers together and divides by 2.
    average = (num1 + num2) / 2
    return average

def main():
    # Ask the user to input two numbers.
    # The inputs are converted to float to allow for decimal numbers.
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Call the calculate_average function with the user inputs.
    result = calculate_average(num1, num2)
    
    # Print out the result.
    print(f"The average of {num1} and {num2} is {result}")

# The entry point of the program
if __name__ == "__main__":
    main()
