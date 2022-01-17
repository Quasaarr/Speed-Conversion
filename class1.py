import config
speed_input = config.speed_input
accuracy_input = config.accuracy_input
desired_unit_input = config.desired_unit

class ConvertSpeedM:
    def m_t_m(self):
        if desired_unit_input.upper() == "M":
            print(f"You were going {speed_input.__round__(accuracy_input)}mph!", "\n")

    def m_t_k(self):
        if desired_unit_input.upper() == "K":
            feet_h = speed_input * 5280
            meters_h = feet_h * 0.3048
            outcome = meters_h / 1000
            print(f"You were going {outcome.__round__(accuracy_input)}km/h!", "\n")

    def m_t_kn(self):
        if desired_unit_input.upper() == "KN":
            feet_h = speed_input * 5280
            outcome = feet_h / 6076
            print(f"You were going {outcome.__round__(accuracy_input)} knots!", "\n")

    def m_t_ma(self):
        if desired_unit_input.upper() == "MA":
            feet_h = speed_input * 5280
            knots_h = feet_h / 6076
            outcome = knots_h / 661.7
            print(f"You were going {outcome} mach (at sea level)!", "\n")


class ConvertSpeedK:
    def k_t_k(self):
        if desired_unit_input.upper() == "K":
            print(f"You were going {speed_input.__round__(accuracy_input)}mph!", "\n")

    def k_t_m(self):
        if desired_unit_input.upper() == "M":
            meters_h = speed_input * 1000
            feet_h = meters_h * 3.280839895013
            outcome = feet_h / 5280
            print(f"You were going {outcome.__round__(accuracy_input)}km/h!", "\n")

    def k_t_kn(self):
        if desired_unit_input.upper() == "KN":
            meters_h = speed_input * 1000
            feet_h = meters_h * 3.280839895013
            outcome = feet_h / 6076
            print(f"You were going {outcome.__round__(accuracy_input)} knots!", "\n")

    def k_t_ma(self):
        if desired_unit_input.upper() == "MA":
            meters_h = speed_input * 1000
            feet_h = meters_h * 3.280839895013
            knots_h = feet_h / 6076
            outcome = knots_h / 661.7
            print(f"You were going {outcome.__round__(accuracy_input)} mach (at sea level)!", "\n")