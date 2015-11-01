import tiles
import config
import pprint
from random import choice, randint

__author__ = 'Manuel'

_rooms = ["EnemyRoom", "EmptyRoom"]

# LAYOUT:
# ['S', 'L', 'E', 'V', 'L'],
# ['/', 'V', 'V', '/', '/'],
# ['/', '/', 'E', 'E', 'V'],
# ['/', '/', '/', 'V', '/'],
# ['/', '/', '/', 'E', '/']
_layout = [[tiles.StartingRoom(0, 0), tiles.LootRoom(1, 0, 0), tiles.EnemyRoom(2, 0, 0),
            tiles.EmptyRoom(3, 0, 0), tiles.LootRoom(4, 0, 0)],
           [None, tiles.EmptyRoom(1, 1), tiles.EmptyRoom(2, 1), None, None],
           [None, None, tiles.EnemyRoom(2, 2, 0), tiles.EnemyRoom(3, 2, 0), tiles.EmptyRoom(4, 2)],
           [None, None, None, tiles.EmptyRoom(3, 3), None],
           [None, None, None, tiles.BossRoom(3, 4, 0), None]]

lvl = 0
_world = {}
start_pos = (0, 0)


def create_layout(cols, rows):
    """
    Crea un layout aleatorio para el mapa
    ¡ROTO!
    """
    loot_count = 0
    # boss_created = False
    layout = []
    for y in range(cols):
        tile = []
        for x in range(rows):
            n = randint(0, 10)
            if n == 0 and loot_count < 2:
                room = "LootRoom"
                loot_count += 1
            elif 0 < n < 6:
                room = choice(_rooms)
            else:
                room = None

            if room is not None:
                tile.append(getattr(__import__('tiles'), room)(x, y, lvl))
            else:
                tile.append(None)
        layout.append(tile)

    layout[0][0] = tiles.StartingRoom(0, 0)
    return layout


def create_world():
    """
    Crea un layout del mapa con la funcion create_layout(cols, rows)
    y la mete en un diccionario.
    """
    # layout = create_layout(5, 5)

    for y in range(len(_layout)):
        for x in range(len(_layout[y])):
            _world[x, y] = _layout[y][x]


def test():
    """
    Imprime el layout del mapa de una manera mas amigable
    a la vista
    """
    if config.DEBUG:
        layout = create_layout(5, 5)
        for y in range(5):
            for x in range(5):
                layout[x][y] = layout[x][y].name if layout[x][y] is not None else '/'
        pp = pprint.PrettyPrinter(4)
        pp.pprint(layout)
        return layout
    else:
        print("""
        -----------------------------
        HABILITAR DEBUG ANTES DE USAR
        world.test()
        -----------------------------
        """)


def tile_exists(x, y):
    """
    Si una habitacion existe en el mapa la devuelve
    """
    return _world.get((x, y))
