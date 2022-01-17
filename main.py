from class1 import ConvertSpeedM
from class1 import ConvertSpeedK
from class2 import ConvertSpeedKN
from class2 import ConvertSpeedMA
from config import Speed
from config import Accuracy
from config import Desired_Unit


line_break = "\n"

# Program Introduction
print("""
This is a high precision speed converter that currently includes 4 units. 
Miles per hour, Kilometers per hour, Knots, and Mach!
All conversion formulas are from NASA's official website! 
""")

# Program Loop
while True:
    Speed()

# Unit-Input Loop
    while True:
        unit = str(input("What unit of speed? (M)ph, (K)m/h, (Kn)ots, or (Ma)ch? "))
        if unit.upper() in ("M", "K", "KN", "MA"):
            break
        print("Please input (M)ph, (K)m/h, (Kn)ots, or (Ma)ch!", line_break)
        continue

# Desired_Unit-Input Loop
    Desired_Unit()

    Accuracy()

    if unit.upper() == "M":
        class1.ConvertSpeedM.m_t_m()
        class1.ConvertSpeedM.m_t_k()
        class1.ConvertSpeedM.m_t_kn()
        class1.ConvertSpeedM.m_t_ma()
    if unit.upper() == "K":
        class1.ConvertSpeedK.k_t_k()
        class1.ConvertSpeedK.k_t_m()
        class1.ConvertSpeedK.k_t_kn()
        class1.ConvertSpeedK.k_t_ma()
    if unit.upper() == "KN":
        class2.ConvertSpeedKN.kn_t_kn()
        class2.ConvertSpeedKN.kn_t_m()
        class2.ConvertSpeedKN.kn_t_k()
        class2.ConvertSpeedKN.kn_t_ma()
    if unit.upper() == "MA":
        class2.ConvertSpeedMA.ma_t_ma()
        class2.ConvertSpeedMA.ma_t_m()
        class2.ConvertSpeedMA.ma_t_k()
        class2.ConvertSpeedMA.ma_t_kn()

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
