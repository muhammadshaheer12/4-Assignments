def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))
    
    # Keep doubling the number until it reaches 100 or more
    while curr_value < 100:
        curr_value *= 2  
        print(curr_value, end=" ")  

if __name__ == "__main__":
    main()
