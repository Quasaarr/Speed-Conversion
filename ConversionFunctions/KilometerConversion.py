class ConvertSpeedK:
    def k_t_k(self, speed, unit, desired_unit, accuracy):
        if unit == (desired_unit == ("K" or "KM")):
            print(speed.__round__(accuracy))

    def k_t_m(self, speed, unit, desired_unit, accuracy):
        if unit == ("K" or "KM") and desired_unit == ("M" or "MP"):
            meters_h = speed * 1000
            feet_h = meters_h * 3.280839895013
            outcome = feet_h / 5280
            print(outcome.__round__(accuracy))

    def k_t_kn(self, speed, unit, desired_unit, accuracy):
        if unit == ("K" or "KM") and desired_unit == "KN":
            meters_h = speed * 1000
            feet_h = meters_h * 3.280839895013
            outcome = feet_h / 6076
            print(outcome.__round__(accuracy))

    def k_t_ma(self, speed, unit, desired_unit, accuracy):
        if unit == ("K" or "KM") and desired_unit == "MA":
            meters_h = speed * 1000
            feet_h = meters_h * 3.280839895013
            knots_h = feet_h / 6076
            outcome = knots_h / 661.7
            print(outcome.__round__(accuracy))