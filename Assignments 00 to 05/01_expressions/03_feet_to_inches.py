def main():
    # Prompt the user to enter a length in feet
    feet = float(input("Enter length in feet: "))
    
    # Convert feet to inches
    inches = feet * 12

    # Display the result
    print(f"{feet} feet is {inches} inches.")

if __name__ == "__main__":
    main()
