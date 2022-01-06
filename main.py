while True:
    # Speed-Input Loop
    while True:
        try:
            speed = int(input("Speed? "))
            break
        except ValueError:
            print("Numerical Values ONLY!")

    # Unit-Input Loop
    while True:
       unit = input("(M)ph or (K)ph? ")
       if unit.upper() in ("M", "K"):
           break
       print("Please input (M)ph or (K)ph!")
       continue
    if unit.upper() == "M":
        converted_speed = speed * 1.60934
        print(f"You were going {converted_speed}kph!")
    if unit.upper() == "K":
        converted_speed = speed / 1.60934
        print(f"You were going {converted_speed}mph!")

    # Repeat-Input Loop
    while True:
        answer = str(input("Run again? (Y/N): "))
        if answer.upper() in ("Y", "N"):
            break
        print("Invalid input.")
    if answer.upper() == "Y":
        continue
    if answer.upper() == "N":
        print("Goodbye! Thank you for using this program!")
        break





