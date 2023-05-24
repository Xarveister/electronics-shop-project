import os
import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, item_name: str):
        if len(item_name) > 10:
            raise Exception("Длина наименования товара превышает 10 символов")
        else:
            self.__name = item_name

    @classmethod
    def instantiate_from_csv(cls) -> None:
        Item.all = []
        with open('C:/Users/Евгений/PycharmProjects/electronics-shop-project/src/items.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                item = Item(name, price, quantity)
                Item.all.append(item)

    @staticmethod
    def string_to_number():
        """метод, возвращающий число из числа-строки"""
        a = float(line)
        return int(a)

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
