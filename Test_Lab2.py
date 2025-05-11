import Lab2

def test_average():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test = 36.857142857142854
    result = Lab2.calc_average_temperature(input_arr)
    assert (result == test)

def test_minmax():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test = [11, 90]
    result = Lab2.calc_min_max_temperature(input_arr)
    assert (result == test)

def test_median():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test = 25
    result = Lab2.calc_median_temperature(input_arr)
    assert (result == test)

