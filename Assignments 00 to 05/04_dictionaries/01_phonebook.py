def main():
    phonebook = {} 

    while True:
        # Display the phonebook menu options to the user.
        print("\nPhonebook Menu:")
        print("1. Add a contact")
        print("2. Search for a contact")
        print("3. Display all contacts")
        print("4. Exit")
        
        # Prompt the user to choose an option.
        choice = input("Choose an option: ")

        if choice == '1':
            # Option 1: Add a contact.
            name = input("Enter the contact name: ")  
            phone_number = input("Enter the phone number: ")  
            phonebook[name] = phone_number  
            print(f"Contact for {name} added successfully!")  
        elif choice == '2':
            # Option 2: Search for a contact.
            name = input("Enter the name you want to search for: ") 
            if name in phonebook:
                # If the name is found in the dictionary, display the contact's phone number.
                print(f"{name}'s phone number is {phonebook[name]}")
            else:
                # If the name is not found, inform the user.
                print(f"Sorry, no contact found for {name}.")

        elif choice == '3':
            # Option 3: Display all contacts.
            if phonebook:
                # If the phonebook is not empty, display all contacts.
                print("\nPhonebook Contacts:")
                for name, phone_number in phonebook.items():
                    # Print each contact's name and phone number.
                    print(f"{name}: {phone_number}")
            else:
                # If the phonebook is empty, inform the user.
                print("Phonebook is empty.")

        elif choice == '4':
            # Option 4: Exit the program.
            print("Exiting phonebook.")
            break  
        else:
            # Handle invalid choices (anything other than 1, 2, 3, or 4).
            print("Invalid choice. Please try again.")

# Run the main function if the script is executed directly.
if __name__ == "__main__":
    main()
