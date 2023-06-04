import pytest
from src.keyboard import KeyBoard

@pytest.fixture
def get_keyboard():
    return KeyBoard('keyboard_1', 2200, 5)


def test_init(get_keyboard):
    keyboard = get_keyboard
    assert keyboard.name == "keyboard_1"
    assert keyboard.price == 2200
    assert keyboard.quantity == 5
    assert keyboard.language == 'EN'


def test_change_lang(get_keyboard):
    keyboard = get_keyboard
    assert keyboard.language == 'EN'
    keyboard.change_lang()
    assert keyboard.language == 'RU'
    keyboard.change_lang()
    assert keyboard.language == 'EN'