class ConvertSpeedKN:
    def KNtKN(self):
        print(f"You were going {speed.__round__(accuracy)} knots!", "\n")

    def KNtM(self):
        FeetH = speed * 6076
        outcome = FeetH / 5280
        print(f"You were going {outcome.__round__(accuracy)}mph!", "\n")

    def KNtK(self):
        FeetH = speed * 6076
        MetersH = FeetH * 0.3048
        outcome = MetersH / 1000
        print(f"You were going {outcome.__round__(accuracy)}km/h!", "\n")

    def KNtMA(self):
        outcome = speed / 661.7
        print(f"You were going {outcome.__round__(accuracy)} mach (at sea level)!", "\n")


class ConvertSpeedMA:
    def MAtMA:
        print(f"You were going {speed.__round__(accuracy)} mach (at sea level)!", "\n")

    def MAtM:
        KnotsH = speed * 661.7
        FeetH = KnotsH * 6076
        outcome = FeetH / 5280
        print(f"You were going {outcome.__round__(accuracy)}mph!", "\n")

    def MAtK:
        KnotsH = speed * 661.7
        FeetH = KnotsH * 6076
        MetersH = FeetH * 0.3048
        outcome = MetersH / 1000
        print(f"You were going {outcome.__round__(accuracy)}km/h!", "\n")

    def MAtKN:
        outcome = speed * 661.7
        print(f"You were going {outcome.__round__(accuracy)} knots!", "\n")
