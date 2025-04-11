# Constant for Mars gravity relative to Earth
MARS_GRAVITY = 0.378

def main():
    # Prompt the user for weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # Calculate Mars weight
    mars_weight = round(earth_weight * MARS_GRAVITY, 2)
    
    # Print the result
    print("The equivalent on Mars: " + str(mars_weight))

if __name__ == "__main__":
    main()
