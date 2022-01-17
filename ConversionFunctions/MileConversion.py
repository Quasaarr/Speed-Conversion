class ConvertSpeedM:
    def m_t_m(self, speed, desired_unit, accuracy):
        if desired_unit.upper() == "M":
            return speed.__round__(accuracy)

    def m_t_k(self, speed, desired_unit, accuracy):
        if desired_unit.upper() == "K":
            feet_h = speed * 5280
            meters_h = feet_h * 0.3048
            outcome = meters_h / 1000
            return outcome.__round__(accuracy)

    def m_t_kn(self, speed, desired_unit, accuracy):
        if desired_unit.upper() == "KN":
            feet_h = speed * 5280
            outcome = feet_h / 6076
            return outcome.__round__(accuracy)

    def m_t_ma(self, speed, desired_unit, accuracy):
        if desired_unit.upper() == "MA":
            feet_h = speed * 5280
            knots_h = feet_h / 6076
            outcome = knots_h / 661.7
            return outcome.__round__(accuracy)