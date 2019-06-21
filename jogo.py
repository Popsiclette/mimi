from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import uniform, choice

# Variaveis globais
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

def mov_mimi(mimi, teclado, speed, janela):
    global pulo, gravidade, andar, andaresq, pulei, olhar

    if escalada == 0:
        mimi.y = mimi.y + gravidade*janela.delta_time() + pulo*janela.delta_time()
        if mimi.y >= chao:
            mimi.y = chao
            pulo = 0
            if pulei == 1:
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
                    mimi = Sprite("images/mimipuloesq.png", 7)
                else:
                    mimi = Sprite("images/mimipulo.png", 7)
                mimi.set_total_duration(800)
                mimi.x = aux
                mimi.y = auy
                pulo -= 500
        else:
            pulo += 500*janela.delta_time()

        if teclado.key_pressed("RIGHT") and mimi.x < janela.width/2:
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
            mimi.x += speed

        if teclado.key_pressed("LEFT") and mimi.x >= 0:
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


def predioatual(mimi, buildings):
    global predio
    for i in range(len(buildings)):
        if buildings[i].x < mimi.x + mimi.width < buildings[i].x + buildings[i].width:
            predio = buildings[i]


def escalar(mimi, teclado):
    global escalada, predio, olhar, andar, andaresq

    if teclado.key_pressed("UP") and predio.x < mimi.x + mimi.width < predio.x + 30 and olhar == 0:
        if escalada == 0:
            andar = 0
            andaresq = 0
            aux = mimi.x + mimi.width
            auy = mimi.y
            mimi = Sprite("images/mimiescalada.png", 10)
            mimi.set_total_duration(1000)
            mimi.x = aux
            mimi.y = auy
        escalada = 1

    if teclado.key_pressed("UP") and predio.x + predio.width - 50 < mimi.x < predio.x + predio.width and olhar == 1:
        if escalada == 0:
            andar = 0
            andaresq = 0
            aux = mimi.x
            auy = mimi.y
            mimi = Sprite("images/mimiescalaresq.png", 10)
            mimi.set_total_duration(1000)
            mimi.x = aux
            mimi.y = auy
        escalada = 1

    if escalada == 1 and teclado.key_pressed("UP") is False:
        aux = mimi.x
        auy = mimi.y
        if olhar == 1:
            mimi = Sprite("images/mimiparadaesq.png")
        else:
            mimi = Sprite("images/mimiparada.png", 1)
        mimi.x = aux
        mimi.y = auy
        mimi.set_total_duration(1000)

    if escalada == 1:
        if mimi.y > predio.y:
            mimi.y -= 1
        else:
            aux = mimi.x
            auy = predio.y
            if olhar == 1:
                mimi = Sprite("images/mimiparadaesq.png")
            else:
                mimi = Sprite("images/mimiparada.png", 1)
            mimi.x = aux
            mimi.y = auy
            mimi.set_total_duration(1000)
        if teclado.key_pressed("UP") is False:
            escalada = 0


    return mimi


def topodopredio(mimi, janela):
    global chao, predio
    if mimi.y <= predio.y and predio.x < mimi.x < predio.x + predio.width:
        chao = predio.y
    else:
        chao = janela.height - 100


# def mov_cenario(mimi, teclado, static, animated, buildings, carnes, speed, janela):
def mov_cenario(mimi, teclado, static, animated, buildings, speed, janela, cao, carros, filhotes):
    global andar, pulo, escalada, ini

    if teclado.key_pressed("RIGHT") and mimi.x >= janela.width/2 and escalada == 0:
        if andar == 0 and pulo == 0:
            aux = mimi.x
            auy = mimi.y
            mimi = Sprite("images/mimiandar.png", 12)
            mimi.x = aux
            mimi.y = auy
            mimi.set_total_duration(1000)
            andar = 1

        ini -= speed
        for i in range(2):
            filhotes[i].x -= speed
        for i in range(len(static)):
            static[i].x -= speed
        for i in range(len(animated)):
            animated[i].x -= speed
        for i in range(len(buildings)):
            buildings[i].x -= speed
        cao.x -= speed
        for i in range(len(carros)):
            carros[i].x -= speed
            # carnes[i].x -= speed

    return mimi


def scrolling(fundo, fundofrente, fundo2, fundo2frente):
    if fundo2.x <= 0:
        fundo.x = fundo2.x + fundo2.width
        fundofrente.x = fundo.x
    if fundo.x <= 0:
        fundo2.x = fundo.x + fundo.width
        fundo2frente.x = fundo2.x


def mov_cao(cao, janela, speed, mimi):
    global olharcao, invertecao
    if 0 <= cao.x <= janela.width:
        if olharcao == 1 and invertecao == 1:
            invertecao = 0
            aux = cao.x
            auy = cao.y
            cao = Sprite("images/dogesq.png", 8)
            cao.x = aux
            cao.y = auy
            cao.set_total_duration(1000)
        elif invertecao == 1:
            invertecao = 0
            aux = cao.x
            auy = cao.y
            cao = Sprite("images/dogdir.png", 8)
            cao.x = aux
            cao.y = auy
            cao.set_total_duration(1000)
        '''if cao.collided(mimi):
            olharcao *= -1
            invertecao = 1'''
    else:
        olharcao *= -1
        invertecao = 1
    cao.x += speed*(-1)*olharcao

    return cao


def mov_carro(carro, speed):
    carro.x -= 2*speed


def cria_carro(janela, altura_rua):
    carros = ["images/carro.png", "images/carro2.png", "images/carro3.png", "images/carro4.png", "images/carro5.png"]
    carro = Sprite(choice(carros))
    carro.x = janela.width
    carro.y = altura_rua + 222
    return carro


def colisao(carros, cao, mimi):
    global vidas, imune
    for carro in carros:
        if mimi.collided(carro):
            vidas -= 1
            if vidas >= 0:
                imune = True
                return True
            else:
                derrota()
    if mimi.collided(cao):
            vidas -= 1
            if vidas >= 0:
                imune = True
                return True
            else:
                derrota()
    return False


def derrota():
    quit()


def mov_filhotes(filhotes):
    global ini
    for i in range(2):
        filhotes[i].x += filhotes[i+2]
        if filhotes[i].x > 100:
            aux = filhotes[i].x
            auy = filhotes[i].y
            filhotes[i] = Sprite("images/filhoteesq.png", 6)
            filhotes[i].x = aux
            filhotes[i].y = auy
            filhotes[i].set_total_duration(1000)
            filhotes[i+2] *= -1
        if filhotes[i].x <= ini:
            aux = filhotes[i].x
            auy = filhotes[i].y
            filhotes[i] = Sprite("images/filhote.png", 6)
            filhotes[i].x = aux
            filhotes[i].y = auy
            filhotes[i].set_total_duration(1000)
            filhotes[i+2] *= -1
    return filhotes


def tremebueiro(bueiro):
    aux = bueiro.x
    auy = bueiro.y
    bueiro = Sprite("images/bueirotreme.png", 8)
    bueiro.x = aux
    bueiro.y = auy
    bueiro.set_total_duration(250)

    return bueiro


def explodebueiro(bueiro):
    aux = bueiro.x
    auy = bueiro.y
    bueiro = Sprite("images/bueiroegeiser.png", 11)
    bueiro.x = aux
    bueiro.y = auy - 130
    bueiro.set_total_duration(1000)

    return bueiro


def colisao_bueiro(bueiro, mimi):
    global vidas, imune
    if mimi.collided(bueiro):
            vidas -= 1
            if vidas >= 0:
                imune = True
                return True
            else:
                derrota()
    return False


def jogo(janela):
    global pulo, chao, predio, imune, vidas

    teclado = Window.get_keyboard()

    bombardeiro = Sprite("images/parado.png")
    casa = Sprite("images/casa2.png")
    fundo = GameImage("images/fundoatras.png")
    fundofrente = GameImage("images/fundofrente.png")
    fundo2 = GameImage("images/fundoatras.png")
    fundo2frente = GameImage("images/fundofrente.png")
    mimi = Sprite("images/mimiparada.png", 1)
    cao = Sprite("images/dogesq.png", 8)
    carne = Sprite("images/chicken.png")
    lua = Sprite("images/lua.png")
    bueiro = Sprite("images/bueiroparado.png", 1)
    cao.set_total_duration(1000)
    mimi.set_total_duration(1000)
    animated = [cao, bombardeiro]
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

    predio = buildings[0]
    chao = janela.height - 100
    mimi.y = chao
    cao.y = janela.height - 108
    cao.x += casa.width
    casa.y = altura_rua + 1
    bombardeiro.x = janela.width
    bombardeiro.y = cao.y - 39

    speed = 5
    lua.x += 15

    tempo_car = 0
    rand_car = uniform(2, 6)

    tempo_bueiro = 0
    tempo_geiser = 0
    parar_bueiro = 0
    rand_bueiro = uniform(3, 8)

    escondido = False
    gatescondido = False
    blink3 = blink4 = 0
    cont3 = cont4 = 0
    blink = blink2 = 0
    cont2 = cont = 0

    exclamacao = Sprite("images/exclamacao.png")
    exclamacao.x = janela.width - exclamacao.width - 20
    exclamacao.y = janela.height - exclamacao.height - 20
    exclamacao.hide()


    carros = []

    filhotes = [(Sprite("images/filhoteesq.png", 6)), (Sprite("images/filhote.png", 6)), -1, 1]
    for i in range(2):
        filhotes[i].x = mimi.x + 50
        filhotes[i].y = mimi.y + 15
        filhotes[i].set_total_duration(1000)

    bueiro.x = mimi.x
    bueiro.y = mimi.y + 35
    bueiro.set_total_duration(250)
    esgoto = 0
    colidirbueiro = False
    while True:

        ### piscar exclamação
        if escondido or blink2 > 0.2:
            exclamacao.unhide()
            blink += janela.delta_time()
            cont = 0
            cont2 += janela.delta_time()

        if cont2 >= 0.5:
            exclamacao.hide()
            cont2 = 0
            blink2 = 0
            escondido = False
            carros.append(cria_carro(janela, altura_rua))

        if blink > 0.2:
            exclamacao.hide()
            blink = blink2 = 0
            cont = 1
            escondido = False

        if cont == 1:
            blink2 += janela.delta_time()

        ### piscar mimi
        if gatescondido or blink3 > 0.2:
            mimi.hide()
            blink4 += janela.delta_time()
            cont3 = 0
            cont4 += janela.delta_time()

        if cont4 >= 0.5:
            mimi.unhide()
            cont4 = 0
            blink3 = 0
            gatescondido = False
            imune = False

        if blink4 > 0.2:
            mimi.unhide()
            blink4 = blink3 = 0
            cont3 = 1
            gatescondido = False

        if cont3 == 1:
            blink3 += janela.delta_time()
        ###

        scrolling(fundo, fundofrente, fundo2, fundo2frente)
        fundo.draw()
        fundo2.draw()
        lua.draw()
        fundofrente.draw()
        fundo2frente.draw()

        for i in range(len(buildings)):
            buildings[i].draw()
        #    carnes[i].draw()

        cao.draw()
        cao.update()
        cao = mov_cao(cao, janela, speed, mimi)

        bombardeiro.draw()

        mimi.draw()
        mimi.update()
        mimi = mov_mimi(mimi, teclado, speed, janela)
        mimi = escalar(mimi, teclado)
        mimi = mov_cenario(mimi, teclado, static, animated, buildings, speed, janela, cao, carros, filhotes)

        filhotes = mov_filhotes(filhotes)
        for i in range(2):
            filhotes[i].draw()
            filhotes[i].update()
        exclamacao.draw()

        bueiro.draw()
        bueiro.update()

        for carro in carros:
            carro.draw()
            mov_carro(carro, speed)
            if carro.x + carro.width < 0:
                carros.remove(carro)

        if imune is False:
            gatescondido = colisao(carros, cao, mimi)

        topodopredio(mimi, janela)
        predioatual(mimi, buildings)

        tempo_bueiro += janela.delta_time()
        tempo_car += janela.delta_time()

        if tempo_bueiro >= rand_bueiro and esgoto == 0:
            bueiro = tremebueiro(bueiro)
            esgoto = 1

        if esgoto == 1:
            tempo_geiser += janela.delta_time()

        if tempo_geiser >= 1.5 and esgoto == 1:
            esgoto = 0
            rand_bueiro = 10000000
            bueiro = explodebueiro(bueiro)
            colidirbueiro = True
            tempo_geiser = 0

        if colidirbueiro is True:
            parar_bueiro += janela.delta_time()
            if imune is False:
                gatescondido = colisao_bueiro(bueiro, mimi)

        if parar_bueiro >= 1 and colidirbueiro is True:
            parar_bueiro = 0
            aux = bueiro.x
            auy = bueiro.y
            bueiro = Sprite("images/bueiroparado.png", 1)
            bueiro.x = aux
            bueiro.y = auy + 130
            bueiro.set_total_duration(1000)
            tempo_bueiro = 0
            rand_bueiro = uniform(3, 8)
            colidirbueiro = False

        if tempo_car >= rand_car:
            tempo_car = 0
            rand_car = uniform(2, 6)
            escondido = True

    #    mov_cenario(mimi, teclado, static, animated, buildings, carnes, speed, janela)

        janela.update()
