from menus import game

# Instantiation of main game class
g = game.Game()


# Managing states
def game(g, event):
    if g.currentstate == "Main Menu":
        g.mm.render(event)

    elif g.currentstate == "Tutorial":
        g.t.render(event)

    elif g.currentstate == "Song Select":
        g.ss.render(event)

    elif g.currentstate == "Game":
        g.sr.render(event)

    elif g.currentstate == "End":
        g.e.render(event)


while g.game_running:
    # Get events
    event = g.events()
    game(g, event)
