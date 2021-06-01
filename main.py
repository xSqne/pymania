from menus import songselect, playstage, game, mainmenu

g = game.Game()
mm = mainmenu.MainMenu(g)
ss = songselect.SongSelect(g)
ps = playstage.PlayStage(g)


def game(g, key):
    if g.currentstate == "Main Menu":
        mm.render(key)

    elif g.currentstate == "Song Select":
        ss.render(key)

    elif g.currentstate == "Game":
        ps.render()


while g.game_running:
    key = g.events()
    game(g, key)

