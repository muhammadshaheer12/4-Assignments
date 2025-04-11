def main():
    # Prompt the user to input their height and convert the input to a floating-point number
    height = float(input("How tall are you? "))
    
    # Check if the user's height is greater than or equal to the minimum required height of 50
    if height >= 50:
        # If the height is sufficient, print this message
        print("You're tall enough to ride!")
    else:
        # If the height is insufficient, print this message
        print("You're not tall enough to ride, but maybe next year!")

# Check if this script is being run directly (i.e., not being imported as a module)
if __name__ == "__main__":
    # Execute the main function when the script is run
    main()

