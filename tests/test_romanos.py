from romanos import romans

def test_romans_for_one_is_I():
    assert romans(1) == "I"

def test_romans_for_5_to_V():
    assert romans(5) == "V"

