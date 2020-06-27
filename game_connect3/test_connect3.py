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
    res = move_pc('---', 'x')
    assert res.count('x') == 1
    assert res.count('o') == 0
    assert res.count('-') == 2
    assert len(res) == 3


def test_move_pc_long_line():
    res = move_pc('--------------------------------------------', 'x')
    assert res.count('x') == 1
    assert res.count('o') == 0
    assert res.count('-') == 43
    assert len(res) == 44


def test_move_pc_full_line():
    res = move_pc('xxoxoxoxoxo', 'x')
    assert res == 'Game over'


def test_move_pc_no_line():
    with pytest.raises(ValueError):
        move_pc('', 'x')
