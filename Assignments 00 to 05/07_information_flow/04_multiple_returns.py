# Function to get the user data
def get_user_data():
    # Asking for user's first name
    first_name = input("What is your first name?: ")
    
    # Asking for user's last name
    last_name = input("What is your last name?: ")
    
    # Asking for user's email address
    email = input("What is your email address?: ")
    
    # Return all three pieces of data as a tuple
    return first_name, last_name, email

def main():
    # Call the function to get user data
    user_data = get_user_data()
    
    # Display the received user data
    print(f"Received the following user data: {user_data}")

if __name__ == "__main__":
    main()
