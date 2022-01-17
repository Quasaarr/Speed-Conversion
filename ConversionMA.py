class ConvertSpeedMA:
    def ma_t_ma(self, speed, desired_unit, accuracy):
        if desired_unit.upper() == "MA":
            return speed.__round__(accuracy)

    def ma_t_m(self, speed, desired_unit, accuracy):
        if desired_unit.upper() == "M":
            knots_h = speed * 661.7
            feet_h = knots_h * 6076
            outcome = feet_h / 5280
            return outcome.__round__(accuracy)

    def ma_t_k(self, speed, desired_unit, accuracy):
        if desired_unit.upper() == "K":
            knots_h = speed * 661.7
            feet_h = knots_h * 6076
            meters_h = feet_h * 0.3048
            outcome = meters_h / 1000
            return outcome.__round__(accuracy)

    def ma_t_kn(self, speed, desired_unit, accuracy):
        if desired_unit.upper() == "KN":
            outcome = speed * 661.7
            return outcome.__round__(accuracy)


