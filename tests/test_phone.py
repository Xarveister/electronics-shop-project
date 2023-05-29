import pytest
from src.phone import Phone

phone1 = Phone("Samsung", 15000, 3, 2)
phone2 = Phone("Honor", 25000, 5, 2)


def test_main():
    assert repr(phone1) == "Phone('Samsung', 15000, 3, 2)"
    assert phone1.number_of_sim == 2


def test_add():
    assert phone1 + phone2 == 8


def test_repr():
    assert repr(phone2) == "Phone('Honor', 25000, 5, 2)"
