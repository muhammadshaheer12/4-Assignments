MAX_LENGTH = 3

def shorten(lst):
    # Remove and print elements until the list is MAX_LENGTH long
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()  # Remove from the end
        print("Removing:", removed)

def main():
    # Get list input from the user
    n = int(input("How many items are in your list? "))
    items = []

    for i in range(n):
        item = input(f"Enter item {i + 1}: ")
        items.append(item)

    print("Original list:", items)
    shorten(items)
    print("Shortened list:", items)

if __name__ == "__main__":
    main()
