class ConvertSpeedM:
    def m_t_m(self, speed, unit, desired_unit, accuracy):
        if unit == ("M" or "MP"):
            if desired_unit == ("M" or "MP"):
                print(speed.__round__(accuracy))

    def m_t_k(self, speed, unit, desired_unit, accuracy):
        if unit == ("M" or "MP") and (desired_unit == "K" or "KM"):
            feet_h = speed * 5280
            meters_h = feet_h * 0.3048
            outcome = meters_h / 1000
            print(outcome.__round__(accuracy))

    def m_t_kn(self, speed, unit, desired_unit, accuracy):
        if unit == ("M" or "MP") and desired_unit == "KN":
            feet_h = speed * 5280
            outcome = feet_h / 6076
            print(outcome.__round__(accuracy))

    def m_t_ma(self, speed, unit, desired_unit, accuracy):
        if unit == ("M" or "MP") and desired_unit == "MA":
            feet_h = speed * 5280
            knots_h = feet_h / 6076
            outcome = knots_h / 661.7
            print(outcome.__round__(accuracy))

