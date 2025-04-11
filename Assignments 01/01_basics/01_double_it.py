def main():
    # Prompt the user for a number
    curr_value = int(input("Enter a number: "))

    # While loop that doubles the number until it reaches 100 or more
    while curr_value < 100:
        curr_value *= 2  
        print(curr_value, end=" ") 

if __name__ == "__main__":
    main()
