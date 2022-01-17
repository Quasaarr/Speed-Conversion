import config
speed = config.Speed()
accuracy = config.Accuracy()
desired_unit = config.Desired_Unit()

class ConvertSpeedKN:
    def kn_t_kn(self):
        if desired_unit.upper() == "KN":
            print(f"You were going {speed.__round__(accuracy)} knots!", "\n")

    def kn_t_m(self):
        if desired_unit.upper() == "M":
            feet_h = speed * 6076
            outcome = feet_h / 5280
            print(f"You were going {outcome.__round__(accuracy)}mph!", "\n")

    def kn_t_k(self):
        if desired_unit.upper() == "K":
            feet_h = speed * 6076
            meters_h = feet_h * 0.3048
            outcome = meters_h / 1000
            print(f"You were going {outcome.__round__(accuracy)}km/h!", "\n")

    def kn_t_ma(self):
        if desired_unit.upper() == "MA":
            outcome = speed / 661.7
            print(f"You were going {outcome.__round__(accuracy)} mach (at sea level)!", "\n")


class ConvertSpeedMA:
    def ma_t_ma:
        if desired_unit.upper() == "MA":
            print(f"You were going {speed.__round__(accuracy)} mach (at sea level)!", "\n")

    def ma_t_m:
        if desired_unit.upper() == "M":
            knots_h = speed * 661.7
            feet_h = knots_h * 6076
            outcome = feet_h / 5280
            print(f"You were going {outcome.__round__(accuracy)}mph!", "\n")

    def ma_t_k:
        if desired_unit.upper() == "K":
            knots_h = speed * 661.7
            feet_h = knots_h * 6076
            meters_h = feet_h * 0.3048
            outcome = meters_h / 1000
            print(f"You were going {outcome.__round__(accuracy)}km/h!", "\n")

    def ma_t_kn:
        if desired_unit.upper() == "KN":
            outcome = speed * 661.7
            print(f"You were going {outcome.__round__(accuracy)} knots!", "\n")