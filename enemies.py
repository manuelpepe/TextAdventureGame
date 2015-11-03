import sys
import inspect

__author__ = 'Manuel'

"""
    Los enemigos del juego.
"""

# Agregar:
#     - Araña
#     - Fantasma
#     - Murcielago
#     - Mago
#     - Caballero Fantasma (B)
#     - Bruja


class Enemigo:
    """ La clase principal para los enemigos """

    is_boss = False

    def __init__(self, name, hp, damage):

        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class Soldado(Enemigo):
    lvl = 0

    def __init__(self):
        super().__init__(name="Soldado",
                         hp=10,
                         damage=10)


class Guerrero(Enemigo):
    lvl = 0

    def __init__(self):
        super().__init__(name="Guerrero",
                         hp=20,
                         damage=9)


class Arquero(Enemigo):
    lvl = 0

    def __init__(self):
        super().__init__(name="Arquero",
                         hp=7,
                         damage=10)


class Lancero(Enemigo):
    lvl = 0

    def __init__(self):
        super().__init__(name="Lancero",
                         hp=15,
                         damage=10)


class Araña(Enemigo):
    def __init__(self):
        super().__init__(name="Araña",
                         hp=15,
                         damage=15)


class MaestroDeArmas(Enemigo):
    lvl = 0

    def __init__(self):
        super().__init__(name="Maestro de Armas",
                         hp=35,
                         damage=35)


class DragonRojo(Enemigo):
    lvl = 0

    def __init__(self):
        super().__init__(name="Dragon Rojo",
                         hp=50,
                         damage=25)


def get_lvl_enemies(lvl):
    """
    Devuelve todos los enemigos del nivel

    Args:
        lvl: Nivel en el que se encuentra el jugador
    """
    enemy_list = []

    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and name != "Enemigo":
            if obj.lvl == lvl and not obj.is_boss:
                enemy_list.append(obj)

    return enemy_list


def get_lvl_bosses(lvl):
    """
    Devuelve todos los jefes del nivel

    Args:
        lvl: Nivel en el que se encuentra el jugador
    """
    boss_list = []

    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj) and name != "Enemigo":
            if obj.lvl == lvl and obj.is_boss:
                boss_list.append(obj)

    return boss_list
