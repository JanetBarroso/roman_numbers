from romanos import romans
import pytest
def test_romans_for_one_is_I():
    assert romans(1) == "I"

def test_romans_for_5_to_V():
    assert romans(5) == "V"

def test_romans_for_negatives_or_zero():
    assert romans(-1) == "not possible to convert " \
                         "-1 to romans"
    assert romans(0) == "not possible to convert 0 to romans"