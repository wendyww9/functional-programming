from activity.functional import shortest_word

def test_finds_shortest_word_in_list_of_words():
    assert shortest_word(["from", "swerve", "of", "shore"]) == "of"

def test_finds_shortest_word_in_list_with_one_word():
    assert shortest_word(["bay"]) == "bay"
