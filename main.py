from ConversionFunctions import MileConversion
from ConversionFunctions import KilometerConversion
from ConversionFunctions import KnotConversion
from ConversionFunctions import MachConversion
CM = MileConversion.ConvertSpeedM()
CK = KilometerConversion.ConvertSpeedK()
CKN = KnotConversion.ConvertSpeedKN()
CMA = MachConversion.ConvertSpeedMA()

# Line Break
lb = "\n"

while True:
#Speed Input
    while True:
        try:
            speed = float(input("Speed? "))
            break
        except ValueError:
            print("Numerical Values Only Please!", lb)

#Unit Input
    while True:
        unit_input = input("What unit of speed? Mph, Km/h, Knots, or Mach? ")
        unit = unit_input[0:2].upper()
        if unit in ("MP", "KM", "KN", "MA"):
            break
        print("Please input Mph, Km/h, Knots, or Mach!", lb)
        continue

#Desired Unit Input
    while True:
        desired_unit_input = input("What would you like to convert to? Mph, Kmh, Knots, or Mach? ")
        desired_unit = desired_unit_input[0:2].upper()
        if desired_unit in ("MP", "KM", "KN", "MA"):
            break
        print("Please input Mph, Kmh, Knots, or Mach!", lb)
        continue

#Accuracy Input
    while True:
        round_input = input("Would you like to round? ")
        round = round_input[0].upper()
        if round in "Y":
            while True:
                try:
                    accuracy = int(input("How many decimal points would you like to round to? "))
                    break
                except ValueError:
                    print("Please input integers (whole numbers) only!", lb)
            break
        if round in "N":
            accuracy = 100
            break
        else:
            print("Answer with yes or no please!", lb)
            continue

#Conversion Functions
    CM.m_t_m(speed, unit, desired_unit, accuracy)
    CM.m_t_k(speed, unit, desired_unit, accuracy)
    CM.m_t_kn(speed, unit, desired_unit, accuracy)
    CM.m_t_ma(speed, unit, desired_unit, accuracy)

    CK.k_t_k(speed, unit, desired_unit, accuracy)
    CK.k_t_m(speed, unit, desired_unit, accuracy)
    CK.k_t_kn(speed, unit, desired_unit, accuracy)
    CK.k_t_ma(speed, unit, desired_unit, accuracy)

    CKN.kn_t_kn(speed, unit, desired_unit, accuracy)
    CKN.kn_t_m(speed, unit, desired_unit, accuracy)
    CKN.kn_t_k(speed, unit, desired_unit, accuracy)
    CKN.kn_t_ma(speed, unit, desired_unit, accuracy)

    CMA.ma_t_ma(speed, unit, desired_unit, accuracy)
    CMA.ma_t_m(speed, unit, desired_unit, accuracy)
    CMA.ma_t_k(speed, unit, desired_unit, accuracy)
    CMA.ma_t_kn(speed, unit, desired_unit, accuracy)

#Program Loop Input
    while True:
        repeat_input = str(input("Run again? (Y/N): "))
        repeat = repeat_input.upper
        if repeat in ("Y", "N"):
            break
        print("Input (Y) or (N) please!", lb)
    if repeat == "Y":
        continue
    else:
        print("Goodbye")
        break

