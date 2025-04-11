# Function to return both first and last name
def get_name():
    first_name = "Muhammad"
    last_name = "Shaheer"
    return first_name, last_name  

# Main function that greets the user using both first and last name
def main():
    first_name, last_name = get_name() 
    print(f"Hello, {first_name} {last_name}!")  

# Ensure the main function is called when this script is run
if __name__ == "__main__":
    main()
