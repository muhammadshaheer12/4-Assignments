# Gravity constants for each planet
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    # Prompt the user for their Earth weight
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # Prompt the user for a planet name
    planet = input("Enter a planet: ")

    # Determine gravity based on planet name
    if planet == "Mercury":
        gravity = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity = VENUS_GRAVITY
    elif planet == "Mars":
        gravity = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity = URANUS_GRAVITY
    elif planet == "Neptune":
        gravity = NEPTUNE_GRAVITY
    else:
        print("Invalid planet name.")
        return

    # Calculate and print equivalent weight
    planet_weight = round(earth_weight * gravity, 2)
    print("The equivalent weight on " + planet + ": " + str(planet_weight))

if __name__ == "__main__":
    main()
