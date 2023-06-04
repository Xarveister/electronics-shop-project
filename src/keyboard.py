from src.item import Item


class MixinLang:
    LANGUAGES = ['EN', 'RU']
    eng = True

    def __init__(self):
        self._language = MixinLang.LANGUAGES[0]

    def change_lang(self):
        '''
        Меняет язык раскладки
        на следующий в списке
        доступных языков.
        '''
        if MixinLang.eng:
            self._language = MixinLang.LANGUAGES[1]
            MixinLang.eng = False
            return self
        else:
            self._language = MixinLang.LANGUAGES[0]
            MixinLang.eng = True
            return self

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        raise AttributeError('property language of KeyBoard object has no setter')


class KeyBoard(Item, MixinLang):

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)

    def __repr__(self) -> str:
        return f"{Item.__name__}('{self.name}', {self.price}, {self.quantity})"
