def feet_to_inches(feet):
    inches = feet * 12
    return inches

while True:
    # Ask the user for feet
    feet = float(input("Enter length in feet (or -1 to quit): "))

    if feet == -1:
        break

    # Convert feet to inches
    inches = feet_to_inches(feet)

    # Print the result
    print(f"{feet} feet is equal to {inches} inches")
    print()
