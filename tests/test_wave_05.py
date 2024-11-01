from activity.functional import sorted_valid_passwords

def test_sorts_passwords_excluding_invalid_from_result():
    passwords = ["password", "p@ssword", "z00p", "hello", "password123"]
    expected_result = ['z00p', 'p@ssword', 'password123']

    assert sorted_valid_passwords(passwords) == expected_result
