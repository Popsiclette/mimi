from PPlay.window import *
from PPlay.gameimage import *
import jogo as jogo


def scrolling(fundo, fundofrente, fundo2, fundo2frente, static):
    if fundo2.x <= 0 and fundo.x < fundo2.x:
        fundo.x = fundo2.x + fundo2.width
        fundofrente.x = fundo.x
    if fundo.x <= 0 and fundo2.x < fundo.x:
        fundo2.x = fundo.x + fundo.width
        fundo2frente.x = fundo2.x
    if fundo.x >= 0 and fundo2.x > fundo.x:
        fundo2.x = fundo.x - fundo2.width
        fundo2frente.x = fundo2.x
    if fundo2.x >= 0 and fundo.x > fundo2.x:
        fundo.x = fundo2.x - fundo.width
        fundofrente.x = fundo.x
    for i in range(len(static)):
        static[i].x -= 3


def menu(janela):
    mouse = Window.get_mouse()

    ###### BACKGROUNDS ######
    fundo = GameImage("images/fundoatras.png")
    fundofrente = GameImage("images/fundofrente.png")
    fundo2 = GameImage("images/fundoatras.png")
    fundo2frente = GameImage("images/fundofrente.png")
    fundo.x = fundofrente.x = 0
    fundo.y = fundofrente.y = fundo2.y = fundo2frente.y = -215
    fundo2.x = fundo2frente.x = fundo.width
    static = [fundo, fundofrente, fundo2, fundo2frente]
    #########################

    ######   BUTTONS   ######
    title = GameImage("images/menu/title.png")
    title.x = janela.width/2 - title.width/2
    title.y = 50

    playbtn = GameImage("images/menu/play.png")
    playbtn.x = 110
    scoresbtn = GameImage("images/menu/scores.png")
    scoresbtn.x = janela.width/2 - scoresbtn.width/2
    quitbtn = GameImage("images/menu/quit.png")
    quitbtn.x = janela.width - 110 - quitbtn.width
    howbtn = GameImage("images/menu/howto.png")
    howbtn.x = janela.width/2 - howbtn.width/2

    playbtn.y = scoresbtn.y = quitbtn.y = 320
    howbtn.y = 500

    creditos= GameImage("images/menu/credits.png")
    creditos.x = janela.width - creditos.width - 30
    creditos.y = janela.height - 30
    #########################

    while True:
        scrolling(fundo, fundofrente, fundo2, fundo2frente, static)
        fundo.draw()
        fundo2.draw()
        fundofrente.draw()
        fundo2frente.draw()

        title.draw()

        playbtn.draw()
        scoresbtn.draw()
        quitbtn.draw()
        howbtn.draw()

        creditos.draw()

        if mouse.is_over_object(creditos) and mouse.is_button_pressed(1):
            jogo.darksouls = True

        if mouse.is_over_area((playbtn.x, playbtn.y), (playbtn.x + playbtn.width, playbtn.y + playbtn.height)) and mouse.is_button_pressed(1):
            return 1

        if mouse.is_over_area((scoresbtn.x, scoresbtn.y), (scoresbtn.x + scoresbtn.width, scoresbtn.y + scoresbtn.height)) and mouse.is_button_pressed(1):
            return 3

        if mouse.is_over_area((quitbtn.x, quitbtn.y), (quitbtn.x + quitbtn.width, quitbtn.y + quitbtn.height)) and mouse.is_button_pressed(1):
            exit()

        if mouse.is_over_area((howbtn.x, howbtn.y), (howbtn.x + howbtn.width, howbtn.y + howbtn.height)) and mouse.is_button_pressed(1):
            return 2

        janela.update()
