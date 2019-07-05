from PPlay.window import *

import menu as menu
import jogo as jogo
import ranking as ranking
import tutorial as tutorial
import gameover as gameover
from PPlay.sound import *

janela = Window(1000,600)
janela.set_title("Mimi")
game_state = 0
dificuldade = 1

tema = Sound("sons/jogo.ogg")
tema.set_volume(50)
tema.set_repeat(True)
tema.play()


while True:
    if game_state == 0:
        game_state = menu.menu(janela)
    if game_state == 1:
        game_state = jogo.jogo(janela)
    if game_state == 2:
        game_state = tutorial.tutorial(janela)
    if game_state == 3:
        game_state = ranking.ranking(janela)
    if game_state == 4:
        game_state = gameover.gameover(janela)

    janela.update()
