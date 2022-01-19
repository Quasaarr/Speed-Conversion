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
    while True:
        try:
            speed = float(input("Speed? "))
            break
        except ValueError:
            print("Numerical Values Only Please!", lb)

    while True:
        unit_input = input("What unit of speed? Mph, Km/h, Knots, or Mach? ")
        unit = unit_input[0:2].upper()
        if unit in ("M", "MP", "K", "KM", "KN", "MA"):
            break
        print("Please input Mph, Km/h, Knots, or Mach!", lb)
        continue

    while True:
        desired_unit_input = input("What would you like to convert to? (M)ph, (K)m/h, (Kn)ots, or (Ma)ch? ")
        desired_unit = desired_unit_input[0:2].upper()
        if desired_unit in ("M", "MP", "K", "KM", "KN", "MA"):
            break
        print("Please input Mph, Km/h, Knots, or Mach!", lb)
        continue

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


