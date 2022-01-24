class ConvertSpeedM:
    def m_t_m(self, speed, unit, desired_unit, accuracy):
        if unit == "MP" and desired_unit == "MP":
            print(f"Here is the converted speed: {speed.__round__(accuracy)} mph")

    def m_t_k(self, speed, unit, desired_unit, accuracy):
        if unit == "MP" and desired_unit == "KM":
            feet_h = speed * 5280
            meters_h = feet_h * 0.3048
            outcome = meters_h / 1000
            print(f"Here is the converted speed: {outcome.__round__(accuracy)} kmh")

    def m_t_kn(self, speed, unit, desired_unit, accuracy):
        if unit == "MP" and desired_unit == "KN":
            feet_h = speed * 5280
            outcome = feet_h / 6076
            print(f"Here is the converted speed: {outcome.__round__(accuracy)} knots")

    def m_t_ma(self, speed, unit, desired_unit, accuracy):
        if unit == "MP" and desired_unit == "MA":
            feet_h = speed * 5280
            knots_h = feet_h / 6076
            outcome = knots_h / 661.7
            print(f"Here is the converted speed: {outcome.__round__(accuracy)} mach")

