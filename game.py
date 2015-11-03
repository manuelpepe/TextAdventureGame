import world
from player import Player
__author__ = 'Manuel'


def play():
    """
    Loop del juego
    """
    print("\n====================================================================")
    world.create_world()
    player = Player()
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())

    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            print("\nElegí una acción:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input("\nAcción: ")
            print("====================================================================")
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    if action_input == 'i':
                        print(room.intro_text())
                    break

    if not player.is_alive():
        print("PERDISTE!\nIgual no te preocupes, la princesa estaba en otro castillo")
    elif player.victory:
        print("Lo siento, la princesa esta en otro castillo!")

if __name__ == '__main__':
    play()
