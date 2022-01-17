# Convert and Print Loop
    if unit.upper() == "M":
        if desired_unit.upper() == "K":
            converted_speed = speed * 1.6093442101
            print(f"You were going {converted_speed.__round__(accuracy)}km/h!", line_break)
        elif desired_unit.upper() == "KN":
            converted_speed = speed * 0.868976823
            print(f"You were going {converted_speed.__round__(accuracy)} knots!", line_break)
        elif unit.upper() == desired_unit.upper():
            print(f"You were going {speed}mph!", line_break)
        elif desired_unit.upper() == "MA":
            converted_speed = speed / 767.269148
            print(f"You were going {converted_speed.__round__(accuracy)} mach!", line_break)

    if unit.upper() == "K":
        if desired_unit.upper() == "M":
            converted_speed = speed * 0.6213711111
            print(f"You were going {converted_speed.__round__(accuracy)}mph!", line_break)
        elif desired_unit.upper() == "KN":
            converted_speed = speed * 0.5399569444
            print(f"You were going {converted_speed.__round__(accuracy)} knots!", line_break)
        elif unit.upper() == desired_unit.upper():
            print(f"You were going {speed}km/h!", line_break)
        elif desired_unit.upper() == "MA":
            converted_speed = speed / 1234.8
            print(f"You were going {converted_speed.__round__(accuracy)} mach!", line_break)

    if unit.upper() == "KN":
        if desired_unit.upper() == "M":
            converted_speed = speed * 1.1507789973
            print(f"You were going {converted_speed.__round__(accuracy)}mph!", line_break)
        elif desired_unit.upper() == "K":
            converted_speed = speed * 0.0005144443
            print(f"You were going {converted_speed.__round__(accuracy)}km/h!", line_break)
        elif unit.upper() == desired_unit.upper():
            print(f"You were going {speed} knots!", line_break)
        elif desired_unit.upper() == "MA":
            converted_speed = speed / 666.738661
            print(f"You were going {converted_speed.__round__(accuracy)} mach!", line_break)

    if unit.upper() == "MA":
        if desired_unit.upper() == "M":
            converted_speed = speed * 767.269148
            print(f"You were going {converted_speed.__round__(accuracy)}mph!", line_break)
        elif desired_unit.upper() == "K":
            converted_speed = speed * 1234.8
            print(f"You were going {converted_speed.__round__(accuracy)}km/h!", line_break)
        elif desired_unit.upper() == "KN":
            converted_speed = speed * 661.738661
            print(f"You were going {converted_speed.__round__(accuracy)} knots!")
        elif unit.upper() == desired_unit.upper():
            print(f"You were going {speed} mach!", line_break)

https://www.mytecbits.com/tools/unit-converters/ft-to-m#chart
grc.nasa.gov/www/k-12/WindTunnel/Activities/knots_vs_mph.html
https://www.grc.nasa.gov/www/k-12/airplane/sound.html