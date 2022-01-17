line_break = "\n"

# Program Introduction
print("""
This is a high precision speed converter that currently includes 4 units. 
Miles per hour, Kilometers per hour, Knots, and Mach!
All conversion formulas are from NASA's official website! 
""")

# Program Loop
while True:
    # Speed-Input Loop
    while True:
        try:
            speed = float(input("Speed? "))
            break
        except ValueError:
            print("Please input numerical values only!", line_break)

# Unit-Input Loop
    while True:
        unit = input("What unit of speed? (M)ph, (K)m/h, (Kn)ots, or (Ma)ch? ")
        if unit.upper() in ("M", "K", "KN", "MA"):
            break
        print("Please input (M)ph, (K)m/h, (Kn)ots, or (Ma)ch!", line_break)
        continue

# Desired_Unit-Input Loop
    while True:
        desired_unit = input("What would you like to convert to? (M)ph, (K)m/h, (Kn)ots, or (Ma)ch? ")
        if desired_unit.upper() in ("M", "K", "KN", "MA"):
            break
        print("Please input (M)ph, (K)m/h, (Kn)ots, or (Ma)ch!", line_break)
        continue

# Accuracy-Input Loop
    while True:
        try:
            accuracy = int(input("How many decimal points would you like to round to? "))
            break
        except ValueError:
            print("Please input integers (whole numbers) only!", line_break)

import

# Repeat-Input Loop
    while True:
        answer = str(input("Run again? (Y/N): "))
        if answer.upper() in ("Y", "N"):
            break
        print("Please input (Y) or (N)!", line_break)
    if answer.upper() == "Y":
        continue
    if answer.upper() == "N":
        print("Goodbye! Thank you for using this program!")
        break