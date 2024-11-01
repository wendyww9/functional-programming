from activity.functional import even_nums

def test_finds_even_nums_in_list_of_numbers():
    assert even_nums([1, 2, 8, 3, 4]) == [2, 8, 4]

def test_finds_even_nums_in_list_with_duplicates():
    assert even_nums([2, 2, 8]) == [2, 2, 8]

