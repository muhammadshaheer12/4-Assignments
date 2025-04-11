def main():
    # Speed of light constant (m/s)
    C = 299_792_458

    # Prompt the user for mass in kilograms
    mass = float(input("Enter kilos of mass: "))

    # Display formula info
    print("\ne = m * C^2...\n")
    print(f"m = {mass} kg")
    print(f"C = {C} m/s\n")

    # Calculate energy
    energy = mass * C**2

    # Display the result
    print(f"{energy} joules of energy!")

if __name__ == "__main__":
    main()
