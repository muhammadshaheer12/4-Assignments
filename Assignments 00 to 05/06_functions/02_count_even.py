import random

DONE_LIKELIHOOD = 0.3  

def done():
    # This function returns True with probability defined by DONE_LIKELIHOOD
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    # This function prints numbers from 1 to 10, but may stop early if done() returns True
    for i in range(1, 11):
        if done():  
            return  
        print(i, end=" ")

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()  
    print("\nI'm done.")  

if __name__ == "__main__":
    main()
