def main():
    # Loop through numbers from 10 to 19
    for num in range(10, 20):  
        # Check if the number is even
        if num % 2 == 0:
            print(f"{num} even", end=" ")  
            print(f"{num} odd", end=" ")  

if __name__ == "__main__":
    main()  
