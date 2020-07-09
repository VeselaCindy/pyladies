import pytest
from sibenice import *


@pytest.mark.parametrize("text,position,symbol,expected",
                         [('___', 1, 'a', '_a_'), ("111", 0, 'x', 'x11'), ("__", 5, 'a', '__')])
def test_change_symbol(text, position, symbol, expected):
    assert change_symbol(text, position, symbol) == expected


def test_move_success():
    output, success = move('a', 'animal', '______')
    assert output == 'a___a_'
    assert success is True
    output, success = move('a', 'animal', 'a___a_')
    assert output == 'a___a_'
    assert success is True


def test_move_not_success():
    output, success = move('a', 'dog', '___')
    assert output == '___'
    assert success is False


def test_move_invalid_input():
    output, success = move('', 'cat', '___')
    assert output == '___'
    assert success is True
    output, success = move(' ', 'cat', '___')
    assert output == '___'
    assert success is True
    output, success = move('ca', 'cat', '___')
    assert output == '___'
    assert success is True
