import sys
import inspect
from random import randint

__author__ = 'Manuel'

"""
    Los items del juego.
"""


class Item:
    """
    La clase principal para los items
    """

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n-----\n{}\nValor: {}".format(self.name,
                                                 self.description,
                                                 self.value)


class Arma(Item):
    """
    Clase base para las armas
    """

    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n-----\n{}\nValor: {}\nDaño: {}".format(self.name, self.description, self.value, self.damage)


class Oro(Item):

    def __init__(self, amount=randint(1, 15)):
        self.amount = amount
        super().__init__(name="Oro",
                         description="Una moneda de ${}".format(str(self.amount)),
                         value=self.amount)


class Piedra(Arma):
    def __init__(self):
        super().__init__(name="Piedra",
                         description="Una simple piedra.",
                         value=0,
                         damage=5)


class Daga(Arma):
    def __init__(self):
        super().__init__(name="Daga",
                         description="Una daga de un tamaño no muy grande",
                         value=10,
                         damage=10)


class EspadaDePiedra(Arma):
    def __init__(self):
        super().__init__(name="Espada de Piedra",
                         description="Una espada de piedra, parece bastante buena",
                         value=20,
                         damage=25)


def get_items():
    """
    Devuelve una lista con todos los items del juego
    """
    item_list = []

    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and name not in ["Item", "Arma"]:
            item_list.append(obj)

    return item_list
