from menus import songselect, stagerandom, game, mainmenu, end

g = game.Game()


def game(g, event):
    if g.currentstate == "Main Menu":
        g.mm.render(event)

    elif g.currentstate == "Song Select":
        g.ss.render(event)

    elif g.currentstate == "Game":
        g.sr.render(event)

    elif g.currentstate == "End":
        g.e.render(event)


while g.game_running:
    event = g.events()
    game(g, event)
