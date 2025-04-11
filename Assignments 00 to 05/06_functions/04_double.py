# Function to double the input number
def double(num):
    return num * 2  

# Main function that prompts the user for input and prints the doubled value
def main():
    # Prompt the user for a number and convert the input to an integer
    num = int(input("Enter a number: ")) 
    
    # Call the double function with the user's input and store the result
    result = double(num)  
    
    # Print the result, using an f-string to format the output
    print(f"Double that is {result}")  

# Ensure the main function is called when this script is run
if __name__ == "__main__":
    main()
