from app import calculate_average

def test_calculate_average():
    assert calculate_average([80, 90, 100]) == 90

def test_empty_marks():
    assert calculate_average([]) == 0

def test_single_mark():
    assert calculate_average([75]) == 75
