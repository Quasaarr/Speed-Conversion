class ConvertSpeedKN:
    def kn_t_kn(self, speed, desired_unit, accuracy):
        if desired_unit.upper() == "KN":
            return speed.__round__(accuracy)

    def kn_t_m(self, speed, desired_unit, accuracy):
        if desired_unit.upper() == "M":
            feet_h = speed * 6076
            outcome = feet_h / 5280
            return outcome.__round__(accuracy)

    def kn_t_k(self, speed, desired_unit, accuracy):
        if desired_unit.upper() == "K":
            feet_h = speed * 6076
            meters_h = feet_h * 0.3048
            outcome = meters_h / 1000
            return outcome.__round__(accuracy)

    def kn_t_ma(self, speed, desired_unit, accuracy):
        if desired_unit.upper() == "MA":
            outcome = speed / 661.7
            return outcome.__round__(accuracy)



