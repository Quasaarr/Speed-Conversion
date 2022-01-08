line_break = "\n"

# Program Loop
while True:
    # Speed-Input Loop
    while True:
        try:
            speed = int(input("Speed? "))
            break
        except ValueError:
            print("Please input numerical values only!", line_break)

# Unit-Input Loop
    while True:
       unit = input("What unit of speed? (M)ph or (K)m/h or (KN)ots? ")
       if unit.upper() in ("M", "K", "KN"):
           break
       print("Please input (M)ph or (K)m/h or (KN)ots!", line_break)
       continue

# Desired_Unit-Input Loop
    while True:
       desired_unit = input("What would you like to convert to? (M)ph or (K)m/h or (KN)ots? ", line_break)
       if desired_unit.upper() in ("M", "K", "KN"):
           break
       print("Please input (M)ph or (K)m/h or (KN)ots!", line_break)
       continue

# Convert and Print Speed
    if unit.upper() == "M":
        if desired_unit.upper() == "K":
            converted_speed = speed * 1.609344
            print(f"You were going {converted_speed}km/h!", line_break)
        if desired_unit.upper() == "KN":
            converted_speed = speed * 1.150779
            print(f"You were going {converted_speed}knots!", line_break)
        if unit.upper() == desired_unit.upper():
            print(f"You were going {speed}mph!", line_break)
    if unit.upper() == "K":
        if desired_unit.upper() == "M":
            converted_speed = speed / 1.609344
            print(f"You were going {converted_speed}mph!", line_break)
        if desired_unit.upper() == "KN":
            converted_speed = speed * 1.852
            print(f"You were going {converted_speed}knots!", line_break)
        if unit.upper() == desired_unit.upper():
            print(f"You were going {speed}km/h!", line_break)
    if unit.upper() == "KN":
        if desired_unit.upper() == "M":
            converted_speed = speed * 0.868976
            print(f"You were going {converted_speed}mph!", line_break)
        if desired_unit.upper() == "K":
            converted_speed = speed * 0.621371
            print(f"You were going {converted_speed}km/h!", line_break)
        if unit.upper() == desired_unit.upper():
            print(f"You were going {speed}knots!", line_break)

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





