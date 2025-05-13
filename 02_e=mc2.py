# Define the speed of light constant
C = 299792458  # m/s

while True:
    # Ask the user for mass in kilograms
    mass = float(input("Enter kilos of mass (or -1 to quit): "))

    if mass == -1:
        break

    # Calculate the energy using Einstein's formula
    energy = mass * (C ** 2)

    # Print the result
    print(f"e = m * C^2... m = {mass} kg, C = {C} m/s")
    print(f"{energy} joules of energy!")
    print()
