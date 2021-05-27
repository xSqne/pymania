import game

g = game.Game()
state = "Main Menu"


def game(g, key):
    if g.currentstate == "Main Menu":
        g.mainmenu_handler(key)

    elif g.currentstate == "Song Select":
        g.songselect_handler(key)


while g.game_running:
    key = g.events()
    game(g, key)

