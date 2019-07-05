from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *


def tutorial(janela):
    keyboard = janela.get_keyboard()

    ###### BACKGROUNDS ######
    fundo = GameImage("images/fundoatras.png")
    fundo.x = 0
    fundo.y = -215
    #########################

    ###### INSTRUCTIONS #####
    walk = GameImage("images/menu/walk.png")
    walk.x = 80
    walk.y = 25
    climb = GameImage("images/menu/climb.png")
    climb.x = 184
    climb.y = 169
    jump = GameImage("images/menu/jump.png")
    jump.x = 80
    jump.y = 385
    esc = GameImage("images/menu/esc.png")
    esc.x = janela.width/2 - esc.width/2
    esc.y = janela.height - esc.height - 25
    #########################

    ######     MIMI    ######
    walking = Sprite("images/mimiandar.png", 12)
    walking.set_total_duration(1000)
    walking.x = 219 - walking.width/2
    walking.y = 71 - walking.height/2
    climbing = Sprite("images/mimiescalada.png", 10)
    climbing.set_total_duration(900)
    climbing.x = 219 - climbing.width/2
    climbing.y = 231 - climbing.height
    jumping = Sprite("images/mimipulo.png", 7)
    jumping.set_total_duration(800)
    jumping.x = 219 - jumping.width/2
    jumping.y = 401 - jumping.height
    #########################

    while True:
        fundo.draw()
        
        walk.draw()
        walking.draw()
        walking.update()
        climb.draw()
        climbing.draw()
        climbing.update()
        jump.draw()
        jumping.draw()
        jumping.update()

        esc.draw()

        if keyboard.key_pressed("ESC"):
            return 0

        janela.update()
