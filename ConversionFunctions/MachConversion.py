class ConvertSpeedMA:
    def ma_t_ma(self, speed, unit, desired_unit, accuracy):
        if unit and desired_unit == "MA":
            print(speed.__round__(accuracy))

    def ma_t_m(self, speed, unit, desired_unit, accuracy):
        if unit == "MA" and desired_unit == ("M" or "MP"):
            knots_h = speed * 661.7
            feet_h = knots_h * 6076
            outcome = feet_h / 5280
            print(outcome.__round__(accuracy))

    def ma_t_k(self, speed, unit, desired_unit, accuracy):
        if unit == "MA" and desired_unit == ("K" or "KM"):
            knots_h = speed * 661.7
            feet_h = knots_h * 6076
            meters_h = feet_h * 0.3048
            outcome = meters_h / 1000
            print(outcome.__round__(accuracy))

    def ma_t_kn(self, speed, unit, desired_unit, accuracy):
        if unit == "MA" and desired_unit == "KN":
            outcome = speed * 661.7
            print(outcome.__round__(accuracy))