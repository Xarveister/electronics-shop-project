import os
import csv
from src.exc import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> object:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) > 10:
            raise Exception('Длина товара превышает 10 символов.')
        self.__name = value

    @classmethod
    def instantiate_from_csv(cls) -> None:
        cls.all = []
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            data = os.path.join(current_dir, 'items.csv')
            with open(data, encoding="cp1251") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if len(row['name']) == 0 or int(row['price']) < 1 or int(row['quantity']) < 0:
                        raise InstantiateCSVError('Файл item.csv поврежден')
                    cls(row["name"], row["price"], row["quantity"])
            print(cls.all)
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')


@staticmethod
def string_to_number(line: str) -> int:
    """Метод, возвращающий число из числа-строки"""
    a = float(line)
    return int(a)


def __add__(self, other):
    if isinstance(other, Item):
        return self.quantity + other.quantity
    raise ValueError('Складывать можно только объекты Item и дочерние от них.')


def calculate_total_price(self) -> float:
    """
    Рассчитывает общую стоимость конкретного товара в магазине.

    :return: Общая стоимость товара.
    """
    return self.price * self.quantity


def apply_discount(self):
    """
    Применяет установленную скидку для конкретного товара.
    """
    self.price = int(self.price * self.pay_rate)
