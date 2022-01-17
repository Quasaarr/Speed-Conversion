speed_input = float(input("Speed? "))
accuracy_input = int(input("How many decimal points would you like to round to? "))
desired_unit = input("What would you like to convert to? (M)ph, (K)m/h, (Kn)ots, or (Ma)ch? ")

def Speed(speed_input):
    while True:
        try:
            speed_input = float(input("Speed? "))
            break
        except ValueError:
            print("Please input numerical values only!", "\n")
        continue


def Accuracy():
    while True:
        try:
            accuracy_input
            break
        except ValueError:
            print("Please input integers (whole numbers) only!", "\n")
        continue


def Desired_Unit():
    while True:
        desired_unit
        if desired_unit.upper() in ("M", "K", "KN", "MA"):
            break
        print("Please input (M)ph, (K)m/h, (Kn)ots, or (Ma)ch!", line_break)
        continue