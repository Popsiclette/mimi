from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import choice

# Variaveis globais
gravidade = 250
pulo = 0
escalada = 0
predio = 0


def mov_mimi(mimi, teclado, speed, janela):
    global pulo, gravidade

    if escalada == 0:
        mimi.y = mimi.y + gravidade*janela.delta_time() + pulo*janela.delta_time()
        if mimi.y >= janela.height - 142:
            mimi.y = janela.height - 142
            pulo = 0
            if teclado.key_pressed("SPACE"):
                pulo -= 500
        else:
            pulo += 500*janela.delta_time()

    if teclado.key_pressed("RIGHT") and mimi.x < janela.width/2:
        mimi.x += speed

    if teclado.key_pressed("LEFT") and mimi.x >= 0:
        mimi.x -= speed


def escalar(mimi, teclado, buildings):
    global escalada, predio

    for i in range(len(buildings)):
        if teclado.key_pressed("UP") and mimi.x + mimi.width > buildings[i].x:
            escalada = 1
            predio = buildings[i]

    if escalada == 1:
        mimi.y -= 1
        for i in range(len(buildings)):
            if teclado.key_pressed("UP") is False or mimi.y < predio.y - mimi.height:
                escalada = 0


#def mov_cenario(mimi, teclado, static, animated, buildings, carnes, speed, janela):
def mov_cenario(mimi, teclado, static, animated, buildings, speed, janela):

    if teclado.key_pressed("RIGHT") and mimi.x >= janela.width/2:
        for i in range(len(static)):
            static[i].x -= speed
        for i in range(len(animated)):
            animated[i].x -= speed
        for i in range(len(buildings)):
            buildings[i].x -= speed
            #carnes[i].x -= speed

def scrolling(fundo, fundofrente, fundo2, fundo2frente):
    if fundo2.x <= 0:
        fundo.x = fundo2.x + fundo2.width
        fundofrente.x = fundo.x
    if fundo.x <= 0:
        fundo2.x = fundo.x + fundo.width
        fundo2frente.x = fundo2.x


def jogo(janela):

    teclado = Window.get_keyboard()

    bombardeiro = Sprite("images/parado.png")
    casa = Sprite("images/casa2.png")
    fundo = GameImage("images/fundoatras.png")
    fundofrente = GameImage("images/fundofrente.png")
    fundo2 = GameImage("images/fundoatras.png")
    fundo2frente = GameImage("images/fundofrente.png")
    mimi = Sprite("images/gatinha.png")
    cao = Sprite("images/caozinho.png")
    carne = Sprite("images/chicken.png")
    carro = Sprite("images/carro.png")
    lua = Sprite("images/lua.png")

    animated = [cao, bombardeiro, carro]
    #static = [fundo, fundofrente, carne]
    static = [fundo, fundofrente, fundo2, fundo2frente]

    # casas = ["images/casa.png", "images/casa2.png", "images/casa3.png", "images/casa4.png"]
    level = {
        0 : ["images/casa3.png", 572],
        1 : ["images/casa.png", 923],
        2 : ["images/casa2.png", 1210],
        3 : ["images/casa.png", 1641],
        4 : ["images/predio.png", 2215],
        5 : ["images/casa2.png", 2585],
        6 : ["images/predio.png", 2854],
        7 : ["images/predio.png", 3226],
        8 : ["images/casa3.png", 3566],
        9 : ["images/casa2.png", 3871],
        10 : ["images/casa.png", 4505],
        11 : ["images/casa2.png", 4828],
        12 : ["images/casa.png", 5177],
        13 : ["images/casa2.png", 5918],
        14 : ["images/casa3.png", 6280],
        15 : ["images/predio.png", 6585],
        16 : ["images/casa2.png", 6884]
    }

    fundo.x = 0
    fundo.y -= 368
    fundofrente.x = 0
    fundofrente.y -= 368
    fundo2.x = fundo.width
    fundo2.y -= 368
    fundo2frente.x = fundo.width
    fundo2frente.y -= 368

    altura_rua = janela.height - 340
    buildings = []
    # carnes = []

    #for i in range(15):
    #    buildings.append(Sprite(choice(casas)))
    #    carnes.append(Sprite("images/chicken.png"))
    #    if i != 0:
    #        buildings[i].x = buildings[i-1].x + buildings[i-1].width
    #    else:
    #        buildings[i].x = 0
    #    buildings[i].y = janela.height - 61 - buildings[i].height
    #    carnes[i].x = buildings[i].x + buildings[i].width / 2 - carne.width / 2
    #    carnes[i].y = buildings[i].y - carne.height/2

    for i in range(17):
        buildings.append(Sprite(level[i][0]))
        buildings[i].x = level[i][1]
        buildings[i].y = janela.height - 61 - buildings[i].height

    mimi.y = janela.height - 142
    cao.y = janela.height - 148
    cao.x += casa.width
    casa.y = altura_rua + 1
    carro.y = altura_rua + 182
    carro.x += cao.x + 100
    bombardeiro.x = janela.width
    bombardeiro.y = cao.y - 39

    speed = 5
    lua.x += 15

    while True:
        scrolling(fundo, fundofrente, fundo2, fundo2frente)
        fundo.draw()
        fundo2.draw()
        lua.draw()
        fundofrente.draw()
        fundo2frente.draw()

        for i in range(len(buildings)):
            buildings[i].draw()
        #    carnes[i].draw()
        mimi.draw()
        cao.draw()
        bombardeiro.draw()
        carro.draw()

        escalar(mimi, teclado, buildings)
        mov_mimi(mimi, teclado, speed, janela)
    #    mov_cenario(mimi, teclado, static, animated, buildings, carnes, speed, janela)
        mov_cenario(mimi, teclado, static, animated, buildings, speed, janela)

        janela.update()
