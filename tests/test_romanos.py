from romanos import romans


def test_romans_for_one_is_I():
    assert romans(1) == "I"


def test_romans_for_5_to_V():
    assert romans(5) == "V"


def test_romans_for_negatives_or_zero():
    assert romans(-1) == "not possible to convert " \
                         "-1 to romans"
    assert romans(0) == "not possible to convert 0 to romans"


def test_romans_for_2():
    assert romans(2) == "II"


def test_romans_for_3():
    assert romans(3) == "III"

