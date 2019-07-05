from PPlay.window import *

import menu as menu
import jogo as jogo
import ranking as ranking
import tutorial as tutorial

janela = Window(1000,600)
janela.set_title("Mimi")
game_state = 3


janela = Window(1000,600)
janela.set_title("Mimi")
game_state = 0
dificuldade = 1

while True:
    if game_state == 0:
        game_state = menu.menu(janela)
    if game_state == 1:
        game_state = jogo.jogo(janela)
    if game_state == 2:
        game_state = tutorial.tutorial(janela)
    if game_state == 3:
        game_state = ranking.ranking(janela)

    janela.update()
