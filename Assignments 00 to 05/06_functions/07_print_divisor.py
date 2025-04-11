def print_divisors(num):
    # Loop through numbers from 1 to num to find divisors
    for i in range(1, num + 1):
        if num % i == 0:  
            print(i, end=" ")  

def main():
    # Prompt the user for input
    num = int(input("Enter a number: "))
    print(f"Here are the divisors of {num}:")
    print_divisors(num)  

if __name__ == "__main__":
    main()  
