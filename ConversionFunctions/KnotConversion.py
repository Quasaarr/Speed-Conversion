class ConvertSpeedKN:
    def kn_t_kn(self, speed, unit, desired_unit, accuracy):
        if unit == "KN" and desired_unit == "KN":
            print(f"Here is the converted speed: {speed.__round__(accuracy)} knots")

    def kn_t_m(self, speed, unit, desired_unit, accuracy):
        if unit == "KN" and desired_unit == "MP":
            feet_h = speed * 6076
            outcome = feet_h / 5280
            print(f"Here is the converted speed: {outcome.__round__(accuracy)} mph")

    def kn_t_k(self, speed, unit, desired_unit, accuracy):
        if unit == "KN" and desired_unit == "KM":
            feet_h = speed * 6076
            meters_h = feet_h * 0.3048
            outcome = meters_h / 1000
            print(f"Here is the converted speed: {outcome.__round__(accuracy)} kmh")

    def kn_t_ma(self, speed, unit, desired_unit, accuracy):
        if unit == "KN" and desired_unit == "MA":
            outcome = speed / 661.7
            print(f"Here is the converted speed: {outcome.__round__(accuracy)} mach (at sea level)")
