class ConvertSpeedM:
    def MtM(self):
        print(f"You were going {speed.__round__(accuracy)}}mph!", "\n")

    def MtK(self):
        FeetH = speed * 5280
        MetersH = FeetH * 0.3048
        outcome = MetersH / 1000
        print(f"You were going {outcome.__round__(accuracy)}km/h!", "\n")

    def MtKN(self):
        FeetH = speed * 5280
        outcome = FeetH / 6076
        print(f"You were going {outcome.__round__(accuracy)} knots!", "\n")

    def MtMA(self):
        FeetH = speed * 5280
        KnotsH = FeetH / 6076
        outcome = KnotsH / 661.7
        print(f"You were going {outcome} mach (at sea level)!", "\n")


class ConvertSpeedK:
    def KtK(self):
        print(f"You were going {speed.__round__(accuracy)}}mph!", "\n")

    def KtM(self):
        MetersH = speed * 1000
        FeetH = MetersH * 3.280839895013
        outcome = FeetH / 5280
        print(f"You were going {outcome.__round__(accuracy)}}km/h!", "\n")

    def KtKN(self):
        MetersH = speed * 1000
        FeetH = MetersH * 3.280839895013
        outcome = FeetH / 6076
        print(f"You were going {outcome.__round__(accuracy)}} knots!", "\n")

    def KtMA(self):
        MetersH = speed * 1000
        FeetH = MetersH * 3.280839895013
        KnotsH = FeetH / 6076
        outcome = KnotsH / 661.7
        print(f"You were going {outcome.__round__(accuracy)}} mach (at sea level)!", "\n")

