def main():
    # Dictionary with fruit names and their prices
    fruit_prices = {
        "apple": 1.5,
        "durian": 10.0,
        "jackfruit": 3.0,
        "kiwi": 2.0,
        "rambutan": 5.5,
        "mango": 2.5
    }

    total_cost = 0

    # Loop through each fruit in the dictionary
    for fruit, price in fruit_prices.items():
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += quantity * price  

    print(f"Your total is ${total_cost}")

if __name__ == "__main__":
    main()
