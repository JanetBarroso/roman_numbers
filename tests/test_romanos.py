from romanos import arabic2roman


def test_romans_for_negatives_or_zero():
    assert arabic2roman(-1) == "not possible to convert " \
                               "-1 to romans"
    assert arabic2roman(0) == "not possible to convert 0 to romans"


def test_print_EnteroPalitos():
    assert arabic2roman(2) == "II"


def test_replace5palitos_w_V():
    assert arabic2roman(6) == "VI"
    assert arabic2roman(8) == "VIII"


def test_replace2V_w_X():
    assert arabic2roman(10) == "X"
    assert arabic2roman(36) == "XXXVI"

def test_replace5X_w_L():
    assert arabic2roman(52) == "LII"
    assert arabic2roman(66) == "LXVI"

def test_replace2L_w_C():
    assert arabic2roman(103) == "CIII"
    assert arabic2roman(376) == "CCCLXXVI"

def test_replace5C_w_D():
    assert arabic2roman(503) == "DIII"
    assert arabic2roman(787) == "DCCLXXXVII"

def test_replace2D_w_M():
    assert arabic2roman(3112) == "MMMCXII"