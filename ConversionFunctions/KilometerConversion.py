class ConvertSpeedK:
    def k_t_k(self, speed, unit, desired_unit, accuracy):
        if unit == "KM" and desired_unit == "KM":
            print(f"Here is the converted speed: {speed.__round__(accuracy)} kmh")

    def k_t_m(self, speed, unit, desired_unit, accuracy):
        if unit == "KM" and desired_unit == "MP":
            meters_h = speed * 1000
            feet_h = meters_h * 3.280839895013
            outcome = feet_h / 5280
            print(f"Here is the converted speed: {outcome.__round__(accuracy)} mph")

    def k_t_kn(self, speed, unit, desired_unit, accuracy):
        if unit == "KM" and desired_unit == "KN":
            meters_h = speed * 1000
            feet_h = meters_h * 3.280839895013
            outcome = feet_h / 6076
            print(f"Here is the converted speed: {outcome.__round__(accuracy)} knots")

    def k_t_ma(self, speed, unit, desired_unit, accuracy):
        if unit == "KM" and desired_unit == "MA":
            meters_h = speed * 1000
            feet_h = meters_h * 3.280839895013
            knots_h = feet_h / 6076
            outcome = knots_h / 661.7
            print(f"Here is the converted speed: {outcome.__round__(accuracy)} mach (at sea level)")