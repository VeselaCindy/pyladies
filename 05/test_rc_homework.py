from rc_homework import *
from datetime import datetime


def test_get_num():
    assert get_num('965319/4448') == 9653194448
    assert get_num('abc') is None
    assert get_num('96') == 96
    assert get_num('') is None


def test_check_format():
    assert check_format('965319') is False
    assert check_format('abc') is False
    assert check_format('965319/4448') is True
    assert check_format('1111a1/2222') is False
    assert check_format('111111/2') is False


def test_check_dates():
    assert check_dates('965318/4620') is True
    assert check_dates('960118/4620') is True
    assert check_dates('961202/2222') is True
    assert check_dates('105318/4620') is True
    assert check_dates('965318') is True
    assert check_dates('966118') is True
    assert check_dates('19965318') is False
    assert check_dates('118523/1111') is False
    assert check_dates('111199') is False


def test_divisibility():
    assert divisibility('999999/9999') is True
    assert divisibility('950901/2150') is True
    assert divisibility('99') is True
    assert divisibility('123456/7890') is False
    assert divisibility('1') is False


def test_get_birthday():
    assert get_birthday('950901/2150') == 'Date of birth: 1.9.1995'
    assert get_birthday('031201/0149') == 'Date of birth: 1.12.2003'
    assert get_birthday('036201/0154') == 'Date of birth: 1.12.2003'


def test_get_sex():
    assert get_sex('950901/2150') == 'Male'
    assert get_sex('031201/0149') == 'Male'
    assert get_sex('036201/0149') == 'Female'
    assert get_sex('035101/0149') == 'Female'
