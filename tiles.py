import items, enemies, actions, world
import config
from random import choice

__author__ = 'Manuel'

"""
    Las habitaciones del juego
"""

DIALOG_INTROS_ALIVE = [
    "¡Oh no! Un {} salvaje aparecio",
    "¡Te encontraste con un {}!",
    "¡Cuidado! ¡Un {} enemigo!"
]

DIALOG_INTROS_DEAD = [
    "El cuerpo de un {} enemigo muerto yace en el piso.",
    "Ves el cuerpo de un {} muerto."
]

DIALOG_EMPTY_ROOM = [
    "Un pasillo vacio",
    "Parece no haber nada",
    "Aca no hay nada"
]

DIALOG_BOSS_ALIVE = [
    "BOSS_INTRO_ALIVE"
]

DIALOG_BOSS_DEAD = [
    "BOSS_INTRO_DEAD"
]


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """ Devuelve todas las direcciones en las que el jugador puede moverse."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """ Devuelve todas las acciones posibles en la habitacion actual."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves


class StartingRoom(MapTile):
    if config.DEBUG:
        name = "S"

    def intro_text(self):
        return """
Estás frente a la puerta del castillo.
Por dentro sabes que deberias ir hacia adelante para entrar al castillo y
buscar a la princesa, pero por dentro sentís un miedo que quiere que vayas
hacia atras. """

    def modify_player(self, player):
        # Sin acción
        pass


class LootRoom(MapTile):
    if config.DEBUG:
        name = "L"

    def __init__(self, x, y, *args):
        item = choice(items.get_items())()

        # while item in player.inventory():
        #     item = choice(items.get_items())()

        self.item = item
        super().__init__(x, y)

    def modify_player(self, player):
        self.add_loot(player)

    def intro_text(self):
        return "¡Encontraste el item: {}!\nLo agarraste".format(self.item.name)

    def add_loot(self, player):
        """ Agrega el item al inventario del jugador

        Args:
            player: El jugador
        """
        player.inventory.append(self.item)


class EmptyRoom(MapTile):
    if config.DEBUG:
        name = "V"

    def __init__(self, x, y, *args):
        self.intro = choice(DIALOG_EMPTY_ROOM)
        super().__init__(x, y)

    def intro_text(self):
        return self.intro

    def modify_player(self, player):
        pass


class EnemyRoom(MapTile):
    if config.DEBUG:
        name = "E"

    def __init__(self, x, y, lvl):
        enemy = choice(enemies.get_lvl_enemies(lvl))()

        self.enemy = enemy
        self.intro_alive = choice(DIALOG_INTROS_ALIVE)
        self.intro_dead = choice(DIALOG_INTROS_DEAD)
        super().__init__(x, y)

    def intro_text(self):
        if self.enemy.is_alive():
            text = self.intro_alive
        else:
            text = self.intro_dead
        return text.format(self.enemy.name)

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("El enemigo te hizo {} de daño. Te quedan {} de HP.".format(self.enemy.damage, player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Attack(enemy=self.enemy)]
        else:
            moves = self.adjacent_moves()
            moves.append(actions.ViewInventory())
            return moves


class BossRoom(MapTile):
    def __init__(self, x, y, lvl):
        boss = choice(enemies.get_lvl_bosses(lvl))()

        self.enemy = boss
        self.intro_alive = choice(DIALOG_BOSS_ALIVE)
        self.intro_dead = choice(DIALOG_BOSS_DEAD)
        super().__init__(x, y)

    def intro_text(self):
        if self.enemy.is_alive():
            text = self.intro_alive
        else:
            text = self.intro_dead

        return text.format(self.enemy.name)

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("El enemigo te hizo {} de daño. Te quedan {} de HP.".format(self.enemy.damage, player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Attack(enemy=self.enemy)]
        else:
            moves = self.adjacent_moves()
            moves.append(actions.ViewInventory())
            moves.append(actions.Win())
            return moves
