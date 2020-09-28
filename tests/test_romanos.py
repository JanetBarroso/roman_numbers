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


def test_replace4_w_IV():
    assert arabic2roman(4) == "IV"
    assert arabic2roman(14) == "XIV"
    assert arabic2roman(64) == "LXIV"

def test_replace9_w_IX():
    assert arabic2roman(9) == "IX"
    assert arabic2roman(39) == "XXXIX"

def test_replace_40_w_XL():
    assert arabic2roman(40) == "XL"
    assert arabic2roman(49) == "XLIX"

def test_replace_90_w_XL():
    assert arabic2roman(90) == "XC"
    assert arabic2roman(199) == "CXCIX"

def test_replace_400_w_CD():
    assert arabic2roman(492) == "CDXCII"
    assert arabic2roman(438) == "CDXXXVIII"

def test_replace_900_w_CM():
    assert arabic2roman(983) == "CMLXXXIII"
    assert arabic2roman(902) == "CMII"