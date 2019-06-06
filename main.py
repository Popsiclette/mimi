from PPlay.window import *

import menu as menu
import jogo as jogo

janela = Window(1000,600)
janela.set_title("Mimi")
game_state = 1
dificuldade = 1

while True:
    if game_state == 0:
        #game_state = menu.menu(janela)
        #game_state = 0
        pass
    if game_state == 1:
        game_state = jogo.jogo(janela)

    janela.update()
