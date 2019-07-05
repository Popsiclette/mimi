from PPlay.window import *

import menu as menu
import jogo as jogo
<<<<<<< HEAD
import ranking as ranking

janela = Window(1000,600)
janela.set_title("Mimi")
game_state = 3
=======
import tutorial as tutorial

janela = Window(1000,600)
janela.set_title("Mimi")
game_state = 0
>>>>>>> e9747150f14ad6c006db9ca3021222bd7c96d666
dificuldade = 1

while True:
    if game_state == 0:
        game_state = menu.menu(janela)
    if game_state == 1:
        game_state = jogo.jogo(janela)
    if game_state == 2:
<<<<<<< HEAD
        game_state = jogo.jogo(janela)
    if game_state == 3:
        game_state = ranking.ranking(janela)
=======
        game_state = tutorial.tutorial(janela)
>>>>>>> e9747150f14ad6c006db9ca3021222bd7c96d666

    janela.update()
