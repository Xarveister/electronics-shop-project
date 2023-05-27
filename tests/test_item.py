"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)


@pytest.fixture
def get_item():
    return Item("Телевизор", 10000, 4)


def test_main():
    assert item1.price == 10000
    assert item1.quantity == 20


def test_calculate_total_price():
    item1.calculate_total_price()
    assert 10000 * 20 == 200000


def test_apply_discount():
    item2.apply_discount()
    assert 20000 * Item.pay_rate == 20000
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert isinstance(Item.all[0], Item)


def test_name_too_long_len(get_item):
    """Название товара слишком длинное"""
    with pytest.raises(Exception):
        item = get_item
        item.name = 'ТелефонТелефонТелефон'


def test_repr():
    item1 = Item("Телефон", 20000, 1)
    assert repr(item1) == "Item('Телефон', 20000, 1)"


def test_str():
    item1 = Item("Телефон", 20000, 1)
    assert str(item1) == 'Телефон'
