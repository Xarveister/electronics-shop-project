"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)


def test_main():
    assert item1.price == 10000
    assert item1.quantity == 20


def test_calculate_total_price():
    item1.calculate_total_price()
    assert 10000 * 20 == 200000


def test_apply_discount():
    item2.apply_discount()
    assert 20000 * Item.pay_rate == 20000
