from connect3 import evaluate, move, move_pc
import pytest


def test_evaluate_positive():
    assert evaluate('--x--') == '-'
    assert evaluate('----') == '-'
    assert evaluate('-xxx-oo') == 'x'
    assert evaluate('ooo--') == 'o'
    assert evaluate('ooxx') == '!'


def test_evaluate_wrong_input():
    assert evaluate('') == '!'
    assert evaluate('hhvv') == '!'


def test_move_positive():
    assert move('---', 2, 'x') == '--x'
    assert move('---', 0, 'o') == 'o--'
    assert move('---', -1, 'x') == '--x'


def test_move_wrong_input():
    with pytest.raises(IndexError):
        move('---', 3, 'x')
        move('---', -4, 'v')


def test_move_pc():
    assert move_pc('---')
