from plus import plus_2_num as plus
import pytest


def test_plus():
    assert plus(1, 2) == 3
    assert plus(2, 3) == 5


test_plus()
