def add_three_copies(my_list, data):
    # Add three copies of the data to the list
    for _ in range(3):
        my_list.append(data)

def main():
    # Ask the user for input
    message = input("Enter a message to copy: ")

    # Create an empty list
    my_list = []

    # Print the list before modifying
    print("List before:", my_list)

    # Call the function to add three copies
    add_three_copies(my_list, message)

    # Print the list after modifying
    print("List after:", my_list)

if __name__ == "__main__":
    main()
