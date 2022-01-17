class ConvertSpeedK:
    def k_t_k(self, speed, desired_unit, accuracy):
        if desired_unit.upper() == "K":
            return speed.__round__(accuracy)

    def k_t_m(self, speed, desired_unit, accuracy):
        if desired_unit.upper() == "M":
            meters_h = speed * 1000
            feet_h = meters_h * 3.280839895013
            outcome = feet_h / 5280
            return outcome.__round__(accuracy)

    def k_t_kn(self, speed, desired_unit, accuracy):
        if desired_unit.upper() == "KN":
            meters_h = speed * 1000
            feet_h = meters_h * 3.280839895013
            outcome = feet_h / 6076
            return outcome.__round__(accuracy)

    def k_t_ma(self, speed, desired_unit, accuracy):
        if desired_unit.upper() == "MA":
            meters_h = speed * 1000
            feet_h = meters_h * 3.280839895013
            knots_h = feet_h / 6076
            outcome = knots_h / 661.7
            return outcome.__round__(accuracy)