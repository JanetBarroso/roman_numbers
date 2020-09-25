from romanos import romans, haz_palitos, string_patterns


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


def test_romans_for_4():
    assert romans(4) == "IV"

def test_romans_for_5():
    assert romans(5) == "V"


def test_romans_for_6():
    assert romans(6) == "VI"

def test_haz_palitos():
    assert haz_palitos(3) == "III"


def test_string_patterns():
    assert string_patterns("III") == "III"
    assert string_patterns("IIIII") == "V"
    assert string_patterns("IIIIIIIIII") == "X"


def test_replace_6_8_palitos_w_V():
    assert (string_patterns("IIIIII")) == "VI"
    assert (string_patterns("IIIIIII")) == "VII"
    assert (string_patterns("IIIIIIII")) == "VIII"
    assert (string_patterns("IIIIIIIII")) =="IX"

def test_romans_from1_to5():
    assert (string_patterns("IIII")) == "IV"
    assert (string_patterns("I")) == "I"
    assert (string_patterns("II")) == "II"

def test_replace_palitos_w_X_():
    assert(string_patterns("IIIIIIIIIII")) == "XI"
    assert (string_patterns("IIIIIIIIIIIIIII")) =="XV"
    assert (string_patterns("IIIIIIIIIIIIIIII")) == "XVI"
    assert string_patterns("IIIIIIIIIIIIII") == "XIV"

def test_33():
    assert (string_patterns("IIIIIIIIIIII"
                            "IIIIIIIIIIII"
                            "IIIIIIIII")) == "XXXIII"

def test_36():
    assert (string_patterns("IIIIIIIIIIIII"
                            "IIIIIIIIIIIII"
                            "IIIIIIII")) == "XXXIV"

def test_39():
    assert (string_patterns("IIIIIIIIIIIII"
                            "IIIIIIIIIIIII"
                            "IIIIIIIIIIIII")) == "XXXIX"
