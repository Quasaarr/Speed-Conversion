import ConversionM
import ConversionK
import ConversionKN
import ConversionMA

# Line Break
lb = "\n"

while True:
    while True:
        try:
            speed = float(input("Speed? "))
            break
        except ValueError:
            print("Numerical Values Only!", lb)

    while True:
        unit_input = input("What unit of speed? (M)ph, (K)m/h, (Kn)ots, or (Ma)ch? ")
        unit = unit_input[0].upper()
        if unit in ("M", "K", "KN", "MA"):
            break
        print("Please input (M)ph, (K)m/h, (Kn)ots, or (Ma)ch!", lb)
        continue

    while True:
        desired_unit_input = input("What would you like to convert to? (M)ph, (K)m/h, (Kn)ots, or (Ma)ch? ")
        desired_unit = desired_unit_input[0].upper()
        if desired_unit in ("M", "K", "KN", "MA"):
            break
        print("Please input (M)ph, (K)m/h, (Kn)ots, or (Ma)ch!", lb)
        continue

    while True:
        try:
            accuracy = int(input("How many decimal points would you like to round to? "))
            break
        except ValueError:
            print("Please input integers (whole numbers) only!", lb)
