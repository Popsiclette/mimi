from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import uniform, choice

gravidade = 250
pulo = 0
escalada = 0
predio = 0
andar = 0
andaresq = 0
pulei = 0
olhar = 0
chao = 0
olharcao = 1
invertecao = 0
vidas = 7
imune = False
invertefilhote = 1
inverteu = 0
ini = 0
pegar = 0
direcao = 1
olhapulo = 0


def scrolling(fundo, fundofrente, fundo2, fundo2frente):
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


def mov_mimi(mimi, teclado, speed, janela):
    global pulo, gravidade, andar, andaresq, pulei, olhar, direcao, olhapulo, pegar

    if escalada == 0:
        mimi.y = mimi.y + gravidade*janela.delta_time() + pulo*janela.delta_time()
        if mimi.y >= chao:
            mimi.y = chao
            pulo = 0
            if pulei == 1:
                olhapulo = 0
                pulei = 0
                andar = 0
                andaresq = 0
                aux = mimi.x
                auy = mimi.y
                if olhar == 1:
                    mimi = Sprite("images/mimiparadaesq.png")
                else:
                    mimi = Sprite("images/mimiparada.png", 1)
                mimi.set_total_duration(1000)
                mimi.x = aux
                mimi.y = auy
            if teclado.key_pressed("SPACE"):
                pulei = 1
                aux = mimi.x
                auy = mimi.y
                if olhar == 1:
                    olhapulo = 1
                    mimi = Sprite("images/mimipuloesq.png", 7)
                else:
                    olhapulo = -1
                    mimi = Sprite("images/mimipulo.png", 7)
                mimi.set_total_duration(800)
                mimi.x = aux
                mimi.y = auy
                pulo -= 500
        else:
            pulo += 500*janela.delta_time()

        if teclado.key_pressed("RIGHT") and (mimi.x < janela.width/2 or (direcao == 0 and mimi.x + mimi.width < janela.width) or (direcao == -1 and mimi.x + mimi.width < janela.width)) and olhapulo != 1:
            if andar == 0 and pulo == 0:
                olhar = 0
                andaresq = 0
                aux = mimi.x
                auy = mimi.y
                mimi = Sprite("images/mimiandar.png", 12)
                mimi.x = aux
                mimi.y = auy
                mimi.set_total_duration(1000)
                andar = 1
                pegar = 0
            mimi.x += speed

        if teclado.key_pressed("LEFT") and mimi.x >= 0 and (direcao != -1 or mimi.x > janela.width/2 - mimi.width*2) and olhapulo != -1:
            if andaresq == 0 and pulo == 0:
                olhar = 1
                andar = 0
                aux = mimi.x
                auy = mimi.y
                mimi = Sprite("images/mimiandarpratras.png", 12)
                mimi.x = aux
                mimi.y = auy
                mimi.set_total_duration(1000)
                andaresq = 1
                pegar = 1
            mimi.x -= speed

        if teclado.key_pressed("RIGHT") is False and andar == 1 and pulo == 0:
            andar = 0
            andaresq = 0
            olhar = 0
            aux = mimi.x
            auy = mimi.y
            mimi = Sprite("images/mimiparada.png", 1)
            mimi.set_total_duration(1000)
            mimi.x = aux
            mimi.y = auy

        if teclado.key_pressed("LEFT") is False and andaresq == 1 and pulo == 0:
            andaresq = 0
            andar = 0
            olhar = 1
            aux = mimi.x
            auy = mimi.y
            mimi = Sprite("images/mimiparadaesq.png", 1)
            mimi.set_total_duration(1000)
            mimi.x = aux
            mimi.y = auy

    return mimi


def mov_cenario(mimi, teclado, static, buildings, speed, janela):
    global andar, pulo, escalada, ini, pegar, direcao, olhar, andaresq

    speed *= direcao

    if direcao == 1 and mimi.x + mimi.width > janela.width/2 + 200 and escalada == 0:
        mimi.x -= 1

    if teclado.key_pressed("RIGHT") and mimi.x >= janela.width/2 and escalada == 0 and direcao == 1:
        if andar == 0 and pulo == 0:
            olhar = 0
            aux = mimi.x
            auy = mimi.y
            mimi = Sprite("images/mimiandar.png", 12)
            mimi.x = aux
            mimi.y = auy
            mimi.set_total_duration(1000)
            andar = 1
            andaresq = 0

        ini -= speed
        for i in range(len(static)):
            static[i].x -= speed - 2
        for i in range(len(buildings)):
            buildings[i].x -= speed
        '''if buildings[16].x + buildings[16].width + 100 <= janela.width and pegar == 0:
            direcao = 0'''

    elif teclado.key_pressed("LEFT") and mimi.x <= janela.width/2 + mimi.width and escalada == 0 and direcao == -1:
        if andaresq == 0 and pulo == 0:
            olhar = 1
            aux = mimi.x
            auy = mimi.y
            mimi = Sprite("images/mimiandarpratras.png", 12)
            mimi.x = aux
            mimi.y = auy
            mimi.set_total_duration(1000)
            andar = 0
            andaresq = 1

        ini -= speed
        for i in range(len(static)):
            static[i].x -= speed + 2
        for i in range(len(buildings)):
            buildings[i].x -= speed
        if ini == 0 and pegar == 1:
            direcao = 0

    if pegar == 1 and ini != 0:
        direcao = -1
    if pegar == 0:
        direcao = 1

    return mimi


def menu(janela):
    global pulo, chao, predio, imune, vidas, pegar

    teclado = Window.get_keyboard()

    fundo = GameImage("images/fundoatras.png")
    fundofrente = GameImage("images/fundofrente.png")
    fundo2 = GameImage("images/fundoatras.png")
    fundo2frente = GameImage("images/fundofrente.png")

    mimi = Sprite("images/mimiparada.png", 1)
    mimi.set_total_duration(1000)
    lua = Sprite("images/lua.png")

    lua.x = janela.width/2 - lua.width/2
    lua.y = 20
    static = [fundo, fundofrente, fundo2, fundo2frente]
    fundo.x = 0
    fundo.y -= 3268
    fundofrente.x = 0
    fundofrente.y -= 368
    fundo2.x = fundo.width
    fundo2.y -= 368
    fundo2frente.x = fundo.width
    fundo2frente.y -= 368
    chao = janela.height - 100
    mimi.y = chao
    speed = 5
    buildings = [Sprite("images/casa2.png")]
    outdoor = Sprite("images/play.png")
    for i in range(len(buildings)):
        buildings[i].y = janela.height - 61 - buildings[i].height
        buildings[i].x = janela.width/2 - buildings[i].width
    outdoor.x = buildings[0].x + buildings[0].width/2 - outdoor.width/2
    outdoor.y = buildings[0].y - outdoor.height

    while True:
        scrolling(fundo, fundofrente, fundo2, fundo2frente)
        fundo.draw()
        fundo2.draw()
        lua.draw()
        fundofrente.draw()
        fundo2frente.draw()
        for i in range(len(buildings)):
            buildings[i].draw()
        outdoor.draw()
        mimi = mov_mimi(mimi, teclado, speed, janela)
        mimi = mov_cenario(mimi, teclado, static, buildings, speed, janela)
        mimi.draw()
        mimi.update()

        janela.update()
