import items
import world
from random import randint

__author__ = 'Manuel'


class Player:
    def __init__(self):
        self.inventory = [items.Oro(15), items.EspadaDePiedra()]
        self.hp = 100
        self.location_x, self.location_y = world.start_pos
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        print("\n======================\nInventario:\n")
        for item in self.inventory:
            print(item, '\n')
        print("======================")

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        """
        Elige el mejor arma que tenga el jugador en el inventario
        y le saca al enemigo el daño de dicha arma
        """
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Arma):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        enemy.hp -= best_weapon.damage
        print("Usaste {} contra {}".format(best_weapon.name, enemy.name))
        if not enemy.is_alive():
            print("Mataste a {}!".format(enemy.name))
            # El jugador se cura un valor igual a
            # la vida del enemigo +- un porcentaje aleatorio de ese valor
            cut = randint(10, 30) * enemy.max_hp / 100
            cure = randint(round(enemy.max_hp - cut), round(enemy.max_hp + cut))
            self.hp += cure
            print("Te curaste {} de vida".format(cure))
        else:
            print("A {} le quedan {} de HP".format(enemy.name, enemy.hp))

    def win(self):
        self.victory = True

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)
