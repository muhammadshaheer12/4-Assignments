# Helper function to simulate checking inventory
def num_in_stock(fruit):
    # A dictionary of fruits and their quantities in stock
    inventory = {
        "apple": 50,
        "banana": 30,
        "pear": 1000,
        "orange": 0,
        "mango": 10,
    }

    # Check if the fruit is in the inventory
    if fruit in inventory:
        return inventory[fruit]
    else:
        return 0  

def main():
    # Prompt the user to enter a fruit
    fruit = input("Enter a fruit: ").lower() 

    # Call num_in_stock(fruit) to check how many of that fruit are in stock
    stock = num_in_stock(fruit)

    # Print the result based on the stock count
    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

if __name__ == "__main__":
    main()
