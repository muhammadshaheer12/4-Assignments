def get_first_element(lst):
    # Print the first element in the list
    print("The first element is:", lst[0])

def main():
    # Prompt user to enter the number of elements
    n = int(input("How many elements do you want to add to the list? "))

    # Create an empty list
    user_list = []

    # Prompt user to enter each element
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)

    # Call the function to print the first element
    get_first_element(user_list)

if __name__ == "__main__":
    main()
