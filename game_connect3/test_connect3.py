from game_connect3.connect3 import *


def test_evaluate():
    assert evaluate("--x--") == '-'
    assert evaluate("----") == "-"
    assert evaluate("-xxx-oo") == "x"
    assert evaluate("ooo--") == "o"
    assert evaluate("ooxx") == "!"


def test_evaluate_wrong_input():
    assert evaluate("") == "!"
    assert evaluate("hhvv") == "-"
