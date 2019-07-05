from PPlay.window import *
from PPlay.gameimage import *


def gameover(janela):
    keyboard = janela.get_keyboard()

    ###### BACKGROUNDS ######
    fundo = GameImage("images/fundoatras.png")
    fundo.x = 0
    fundo.y = -215
    #########################

    ###### INSTRUCTIONS #####
    message = GameImage("images/menu/gameover.png")
    message.x = janela.width/2 - message.width/2
    message.y = 80
    esc = GameImage("images/menu/esc.png")
    esc.x = janela.width/2 - esc.width/2
    esc.y = janela.height - esc.height - 25
    #########################

    while True:
        fundo.draw()
        
        message.draw()

        esc.draw()

        if keyboard.key_pressed("ESC"):
            return 0

        janela.update()
