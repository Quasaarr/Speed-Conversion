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

# Convert and Print Loop
    if unit.upper() == "M":
        if desired_unit.upper() == "K":
            converted_speed = speed * 1.6093442101
            print(f"You were going {converted_speed.__round__(accuracy)}km/h!", line_break)
        elif desired_unit.upper() == "KN":
            converted_speed = speed * 0.868976823
            print(f"You were going {converted_speed.__round__(accuracy)} knots!", line_break)
        elif unit.upper() == desired_unit.upper():
            print(f"You were going {speed}mph!", line_break)
        elif desired_unit.upper() == "MA":
            converted_speed = speed / 767.269148
            print(f"You were going {converted_speed.__round__(accuracy)} mach!", line_break)

    if unit.upper() == "K":
        if desired_unit.upper() == "M":
            converted_speed = speed * 0.6213711111
            print(f"You were going {converted_speed.__round__(accuracy)}mph!", line_break)
        elif desired_unit.upper() == "KN":
            converted_speed = speed * 0.5399569444
            print(f"You were going {converted_speed.__round__(accuracy)} knots!", line_break)
        elif unit.upper() == desired_unit.upper():
            print(f"You were going {speed}km/h!", line_break)
        elif desired_unit.upper() == "MA":
            converted_speed = speed / 1234.8
            print(f"You were going {converted_speed.__round__(accuracy)} mach!", line_break)

    if unit.upper() == "KN":
        if desired_unit.upper() == "M":
            converted_speed = speed * 1.1507789973
            print(f"You were going {converted_speed.__round__(accuracy)}mph!", line_break)
        elif desired_unit.upper() == "K":
            converted_speed = speed * 0.0005144443
            print(f"You were going {converted_speed.__round__(accuracy)}km/h!", line_break)
        elif unit.upper() == desired_unit.upper():
            print(f"You were going {speed} knots!", line_break)
        elif desired_unit.upper() == "MA":
            converted_speed = speed / 666.738661
            print(f"You were going {converted_speed.__round__(accuracy)} mach!", line_break)

    if unit.upper() == "MA":
        if desired_unit.upper() == "M":
            converted_speed = speed * 767.269148
            print(f"You were going {converted_speed.__round__(accuracy)}mph!", line_break)
        elif desired_unit.upper() == "K":
            converted_speed = speed * 1234.8
            print(f"You were going {converted_speed.__round__(accuracy)}km/h!", line_break)
        elif desired_unit.upper() == "KN":
            converted_speed = speed * 661.738661
            print(f"You were going {converted_speed.__round__(accuracy)} knots!")
        elif unit.upper() == desired_unit.upper():
            print(f"You were going {speed} mach!", line_break)

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
