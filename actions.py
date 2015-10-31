from player import Player

__author__ = 'Manuel'


class Action:
    def __init__(self, name, hotkey, method, **kwargs):
        self.name = name
        self.hotkey = hotkey
        self.method = method
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north,
                         name='Moverse al Norte',
                         hotkey='n')


class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south,
                         name='Moverse al Sur',
                         hotkey='s')


class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east,
                         name='Moverse al Este',
                         hotkey='e')


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west,
                         name='Moverse al Oeste',
                         hotkey='o')


class ViewInventory(Action):
    def __init__(self):
        super().__init__(method=Player.print_inventory,
                         name='Ver Inventario',
                         hotkey='i')


class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack,
                         name="Atacar",
                         hotkey='a',
                         enemy=enemy)
