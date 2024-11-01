from activity.functional import report

def test_reports_length_function_call():
    expected_result = 'The result of applying len to hello is 5'

    assert report("hello", len, "len") == expected_result

def test_resorts_result_of_calling_lambda():
    expected_result = 'The result of applying upper to people is PEOPLE'

    assert report("people", lambda w: w.upper(), "upper") == expected_result
