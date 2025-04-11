# Define the maximum value for the Fibonacci sequence
MAX_VALUE = 10000

def main():
    # Initialize the first two Fibonacci numbers
    fib_0 = 0
    fib_1 = 1
    
    # Print the first two terms
    print(fib_0, fib_1, end=" ")
    
    # Compute and print the next Fibonacci numbers until we reach the max value
    while True:
        next_fib = fib_0 + fib_1
        if next_fib >= MAX_VALUE:
            break
        print(next_fib, end=" ")
        
        # Update the Fibonacci numbers for the next iteration
        fib_0 = fib_1
        fib_1 = next_fib
    
    print()  
if __name__ == "__main__":
    main()
