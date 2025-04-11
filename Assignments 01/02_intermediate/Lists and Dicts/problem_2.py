# Function to access an element at a given index in the list
def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

# Function to modify an element at a given index in the list
def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

# Function to return a slice of the list from start to end (not including end)
def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices."

# Main function that runs the index game
def index_game():
    # Initial list of pets
    lst = ["cat", "dog", "parrot", "hamster", "goldfish"]
    print("Current list:", lst)
    
    # Prompt user to choose an operation
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ").strip().lower()

    # Perform the corresponding operation based on user input
    if operation == "access":
        # Access element at user-provided index
        index = int(input("Enter index to access: "))
        print("Result:", access_element(lst, index))
    elif operation == "modify":
        # Modify element at a specific index with a new value
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        result = modify_element(lst, index, new_value)
        print("Updated list:", result)
    elif operation == "slice":
        # Get a sublist from start to end index
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print("Sliced list:", slice_list(lst, start, end))
    else:
        # Handle invalid operation input
        print("Invalid operation.")

# Run the index game only if this script is executed directly
if __name__ == "__main__":
    index_game()
