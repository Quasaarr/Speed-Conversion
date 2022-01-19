class ConvertSpeedKN:
    def kn_t_kn(self, speed, unit, desired_unit, accuracy):
        if unit == (desired_unit == "KN"):
            print(speed.__round__(accuracy))

    def kn_t_m(self, speed, unit, desired_unit, accuracy):
        if unit == "KN" and desired_unit == ("M" or "MP"):
            feet_h = speed * 6076
            outcome = feet_h / 5280
            print(outcome.__round__(accuracy))

    def kn_t_k(self, speed, unit, desired_unit, accuracy):
        if unit == "KN" and desired_unit == ("K" or "KM"):
            feet_h = speed * 6076
            meters_h = feet_h * 0.3048
            outcome = meters_h / 1000
            print(outcome.__round__(accuracy))

    def kn_t_ma(self, speed, unit, desired_unit, accuracy):
        if unit == "KN" and desired_unit == "MA":
            outcome = speed / 661.7
            print(outcome.__round__(accuracy))
