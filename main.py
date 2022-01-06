while True:
    try:
        speed = int(input("Speed? "))
    except ValueError:
        print("Numerical Values ONLY!")
        speed = int(input("Speed? "))
    unit = input("(M)ph or (K)ph? ")
    if unit.upper() == "M":
        converted_speed = speed * 1.60934
        print(f"You were going {converted_speed}kph!")
    elif unit.upper() == "K":
        converted_speed = speed / 1.60934
        print(f"You were going {converted_speed}mph!")
    else:
        print("Please input (M)ph or (K)ph!")
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





