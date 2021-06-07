import time

from menus import songselect, playstage, game, mainmenu

g = game.Game()
mm = mainmenu.MainMenu(g)
ss = songselect.SongSelect(g)
ps = playstage.PlayStage(g)


def game(g, event):
    if g.currentstate == "Main Menu":
        mm.render(event)

    elif g.currentstate == "Song Select":
        ss.render(event)

    elif g.currentstate == "Game":
        ps.render()

while g.game_running:
    event = g.events()
    game(g, event)

