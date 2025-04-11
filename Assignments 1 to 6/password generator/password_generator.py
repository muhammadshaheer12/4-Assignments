import random
import string
from termcolor import colored
import pyperclip 

# Function to generate password
def generate_password(length, use_uppercase, use_digits, use_symbols):
    # Define possible characters for password
    lower = string.ascii_lowercase  
    upper = string.ascii_uppercase  
    digits = string.digits          
    symbols = string.punctuation    

    # Combine the character sets based on the user's preferences
    characters = lower  
    if use_uppercase:
        characters += upper  
    if use_digits:
        characters += digits  
    if use_symbols:
        characters += symbols  

    # Generate the password by randomly selecting characters from the available pool
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to evaluate password strength
def evaluate_strength(password):
    if len(password) < 8:
        return colored("🔴 Weak", "red")
    elif len(password) < 12:
        return colored("🟠 Medium", "yellow")
    else:
        return colored("🟢 Strong", "green")

# Function to get user preferences and display the generated password
def get_password_options():
    print(colored("🔐✨ Welcome to the Password Generator! ✨🔐", "green"))
    
    # Get the length of the password from the user
    length = int(input(colored("🔢 Enter the desired length of your password: ", "cyan")))
    
    # Get user preferences for password components
    use_uppercase = input(colored("🔤 Include uppercase letters? (y/n): ", "yellow")).lower() == 'y'
    use_digits = input(colored("🔢 Include digits? (y/n): ", "yellow")).lower() == 'y'
    use_symbols = input(colored("💥 Include special symbols? (y/n): ", "yellow")).lower() == 'y'
    
    # Generate the password
    password = generate_password(length, use_uppercase, use_digits, use_symbols)
    
    # Show the generated password with a message and emojis
    print("\n" + colored("🎉 Your super-secure password is: ", "magenta") + colored(password, "blue"))
    
    # Display password strength
    print(f"💪 Password Strength: {evaluate_strength(password)}")
    
    # Ask if the user wants to copy the password to clipboard
    copy_choice = input(colored("📋 Would you like to copy this password to clipboard? (y/n): ", "cyan")).lower()
    if copy_choice == 'y':
        pyperclip.copy(password)
        print(colored("✅ Password copied to clipboard!", "green"))
    
    # Ask if the user wants to save the password to a file
    save_choice = input(colored("💾 Would you like to save this password to a file? (y/n): ", "cyan")).lower()
    if save_choice == 'y':
        with open("passwords.txt", "a") as file:
            file.write(f"{password}\n")
        print(colored("✅ Password saved to passwords.txt!", "green"))
    
    # Ask if the user wants to regenerate a password
    regenerate = input(colored("\n🔄 Would you like to generate another password? (y/n): ", "cyan")).lower()
    if regenerate == 'y':
        get_password_options()
    else:
        print(colored("\n🚪 Exiting... Stay safe and keep your passwords secure! 🔐", "red"))

# Run the password generator when the script is executed
if __name__ == "__main__":
    get_password_options()
