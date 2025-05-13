import math

# Ask the user for the lengths of the two sides
AB = float(input("Enter the length of AB: "))
AC = float(input("Enter the length of AC: "))

# Calculate the length of the hypotenuse (BC) using the Pythagorean theorem
BC = math.sqrt(AB ** 2 + AC ** 2)

# Print the result
print(f"The length of BC (the hypotenuse) is: {BC}")

