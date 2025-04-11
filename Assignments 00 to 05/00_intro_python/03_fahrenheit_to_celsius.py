def main():
    # Prompt the user for the temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    # Display the result
    print(f"Temperature: {fahrenheit}F = {celsius}C")

# Run the main function
if __name__ == "__main__":
    main()
