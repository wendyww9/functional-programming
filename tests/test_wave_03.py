from activity.functional import squares

def test_calculates_squares_for_list_of_numbers():
    assert squares([1, 2, 8, 3, 4]) == [1, 4, 64, 9, 16]

def test_calculates_squares_for_list_with_duplicates():
    assert squares([2, 2, 8]) == [4, 4, 64]
