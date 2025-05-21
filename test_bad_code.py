from bad_code import calculate_area

def test_calculate_area():
    assert calculate_area(3, 4) == 12
    assert calculate_area(0, 10) == 0
    assert calculate_area(5, 2) == 10