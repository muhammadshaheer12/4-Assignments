def get_last_element(lst):
    # Print the last element in the list
    print("The last element is:", lst[-1])

def main():
    # Prompt the user for the number of elements
    n = int(input("How many elements do you want to add to the list? "))

    # Initialize an empty list
    user_list = []

    # Collect elements from the user
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)

    # Print the last element using the function
    get_last_element(user_list)

if __name__ == "__main__":
    main()
