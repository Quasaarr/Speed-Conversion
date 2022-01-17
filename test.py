from ConversionMA import ConvertSpeedKN
from ConversionMA import ConvertSpeedMA

speed = float(input("Speed? "))
desired_unit = input("What would you like to convert to? (M)ph, (K)m/h, (Kn)ots, or (Ma)ch? ")
accuracy = int(input("How many decimal points would you like to round to? "))
CM = ConvertSpeedMA()
print(CM.ma_t_m(speed, desired_unit, accuracy))
