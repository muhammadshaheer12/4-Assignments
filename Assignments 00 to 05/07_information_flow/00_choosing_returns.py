# Define the constant for the adult age
ADULT_AGE = 18

def is_adult(age):
    # Return True if age is greater than or equal to ADULT_AGE, otherwise False
    if age >= ADULT_AGE:
        return True
    else:
        return False

def main():
    # Prompt the user to enter an age
    age = int(input("How old is this person?: "))
    
    # Call the function to check if the person is an adult and print the result
    print(is_adult(age))

if __name__ == "__main__":
    main()
