from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import *
from random import uniform, choice
import ranking as ranking

'''
  #####                                     
 #     # #       ####  #####    ##   #      
 #       #      #    # #    #  #  #  #      
 #  #### #      #    # #####  #    # #      
 #     # #      #    # #    # ###### #      
 #     # #      #    # #    # #    # #      
  #####  ######  ####  #####  #    # ###### 
'''
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
vidas = 7
imune = False
invertefilhote = 1
inverteu = 0
ini = 0
pegar = 0
direcao = 1
olharpulo = 0
soltoucarne = False
darksouls = False


'''
 #     #                                                                      
 ##   ## # #    # #    #    #  ####  #    # ###### #    # ###### #    # ##### 
 # # # # # ##  ## #    ##  ## #    # #    # #      ##  ## #      ##   #   #   
 #  #  # # # ## # #    # ## # #    # #    # #####  # ## # #####  # #  #   #   
 #     # # #    # #    #    # #    # #    # #      #    # #      #  # #   #   
 #     # # #    # #    #    # #    #  #  #  #      #    # #      #   ##   #   
 #     # # #    # #    #    #  ####    ##   ###### #    # ###### #    #   # 
'''


def mov_mimi(mimi, teclado, speed, janela):
    global pulo, gravidade, andar, andaresq, pulei, olhar, direcao, olharpulo

    if escalada == 0:
        mimi.y = mimi.y + gravidade*janela.delta_time() + pulo*janela.delta_time()
        if mimi.y >= chao:
            mimi.y = chao
            pulo = 0
            if pulei == 1:
                olharpulo = 0
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
                    olharpulo = 1
                    mimi = Sprite("images/mimipuloesq.png", 7)
                else:
                    olharpulo = -1
                    mimi = Sprite("images/mimipulo.png", 7)
                mimi.set_total_duration(800)
                mimi.x = aux
                mimi.y = auy
                pulo -= 550
        else:
            pulo += 550*janela.delta_time()

        if teclado.key_pressed("RIGHT") and (mimi.x < janela.width/2 or (direcao == 0 and mimi.x + mimi.width < janela.width) or (direcao == -1 and mimi.x + mimi.width < janela.width)) and olharpulo != 1:
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

        if teclado.key_pressed("LEFT") and mimi.x >= 0 and (direcao != -1 or mimi.x > janela.width/2 + mimi.width) and olharpulo != -1:
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


'''
 #     #                                                                             
 ##   ## ######   ##   #####     ####   ####  #      #      #  ####  #  ####  #    # 
 # # # # #       #  #    #      #    # #    # #      #      # #      # #    # ##   # 
 #  #  # #####  #    #   #      #      #    # #      #      #  ####  # #    # # #  # 
 #     # #      ######   #      #      #    # #      #      #      # # #    # #  # # 
 #     # #      #    #   #      #    # #    # #      #      # #    # # #    # #   ## 
 #     # ###### #    #   #       ####   ####  ###### ###### #  ####  #  ####  #    # 
'''


def pegarcarne(carne, mimi, janela):
    global pegar, imune, soltoucarne
    if mimi.collided(carne) and imune is False:
        pegar = 1
        carne.y = 40
        carne.x = janela.width - carne.height
        soltoucarne = False
    return carne


def droparcarne(carne, mimi):
    global pegar, soltoucarne
    if pegar == 1:
        pegar = 0
        carne.y = mimi.y
        carne.x = mimi.x
        soltoucarne = True


'''
  #####                                                                                            
 #     # #    # #####  #####  ###### #    # #####    #####  #    # # #      #####  # #    #  ####  
 #       #    # #    # #    # #      ##   #   #      #    # #    # # #      #    # # ##   # #    # 
 #       #    # #    # #    # #####  # #  #   #      #####  #    # # #      #    # # # #  # #      
 #       #    # #####  #####  #      #  # #   #      #    # #    # # #      #    # # #  # # #  ### 
 #     # #    # #   #  #   #  #      #   ##   #      #    # #    # # #      #    # # #   ## #    # 
  #####   ####  #    # #    # ###### #    #   #      #####   ####  # ###### #####  # #    #  ####  
'''


def predioatual(mimi, buildings):
    global predio
    for i in range(19):
        if buildings[i].x - 30 <= mimi.x + mimi.width <= buildings[i].x + buildings[i].width + 30:
            predio = buildings[i]


'''
  #####                         
 #     # #      # #    # #####  
 #       #      # ##  ## #    # 
 #       #      # # ## # #####  
 #       #      # #    # #    # 
 #     # #      # #    # #    # 
  #####  ###### # #    # #####  
'''


def escalar(mimi, teclado, buildings, janela):
    global escalada, olhar, andar, andaresq, predio

    for predios in buildings:
        if 0 <= predios.x + predios.width <= janela.width:
            if teclado.key_pressed("UP") and predios.x < mimi.x + mimi.width < predios.x + 30 and olhar == 0 and mimi.y > predios.y:
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
                predio = predios

            if teclado.key_pressed("UP") and predios.x + predios.width - 50 < mimi.x < predios.x + predios.width and olhar == 1 and mimi.y > predios.y:
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
                predio = predios

    if escalada == 1 and teclado.key_pressed("UP") is False:
        aux = mimi.x
        auy = mimi.y
        if olhar == 1:
            mimi = Sprite("images/mimiparadaesq.png")
            aux -= 10
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
                aux -= 10
            else:
                mimi = Sprite("images/mimiparada.png", 1)
            mimi.x = aux
            mimi.y = auy
            mimi.set_total_duration(1000)
            escalada = 0
    if teclado.key_pressed("UP") is False:
        escalada = 0

    return mimi


'''
 ######                                                                
 #     # #    # # #      #####  # #    #  ####     #####  ####  #####  
 #     # #    # # #      #    # # ##   # #    #      #   #    # #    # 
 ######  #    # # #      #    # # # #  # #           #   #    # #    # 
 #     # #    # # #      #    # # #  # # #  ###      #   #    # #####  
 #     # #    # # #      #    # # #   ## #    #      #   #    # #      
 ######   ####  # ###### #####  # #    #  ####       #    ####  #      
'''


def topodopredio(mimi, janela):
    global chao, predio
    if mimi.y <= predio.y and predio.x - 30 < mimi.x < predio.x + predio.width:
        chao = predio.y
    else:
        chao = janela.height - 100


'''
  #####                                                                                        
 #     #  ####  ###### #    # ###### #####  #   #     ####   ####  #####   ####  #      #      
 #       #    # #      ##   # #      #    #  # #     #      #    # #    # #    # #      #      
  #####  #      #####  # #  # #####  #    #   #       ####  #      #    # #    # #      #      
       # #      #      #  # # #      #####    #           # #      #####  #    # #      #      
 #     # #    # #      #   ## #      #   #    #      #    # #    # #   #  #    # #      #      
  #####   ####  ###### #    # ###### #    #   #       ####   ####  #    #  ####  ###### ###### 
'''


def mov_cenario(mimi, teclado, static, bombardeiro, buildings, speed, janela, cao, carros, filhotes, carne, garrafas, bueiros, lixeiras):
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
        for i in range(len(lixeiras)):
            lixeiras[i].x -= speed
        for i in range(len(garrafas)):
            garrafas[i][0].x -= speed
        for i in range(2):
            filhotes[i].x -= speed
        for i in range(len(static)):
            static[i].x -= speed - 2
        for i in range(len(buildings)):
            buildings[i].x -= speed
        for i in range(len(cao)):
            cao[i].x -= speed
        for i in range(len(bombardeiro)):
            bombardeiro[i][0].x -= speed
        for i in range(len(carros)):
            carros[i].x -= speed
        for i in range(len(bueiros)):
            bueiros[i].x -= speed

        if pegar == 0:
            carne.x -= speed
        if buildings[19].x + buildings[19].width + 100 <= janela.width and pegar == 0:
            direcao = 0

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
        for i in range(len(lixeiras)):
            lixeiras[i].x -= speed
        for i in range(len(garrafas)):
            garrafas[i][0].x -= speed
        for i in range(2):
            filhotes[i].x -= speed
        for i in range(len(bombardeiro)):
            bombardeiro[i][0].x -= speed
        for i in range(len(static)):
            static[i].x -= speed + 2
        for i in range(len(buildings)):
            buildings[i].x -= speed
        for i in range(len(cao)):
            cao[i].x -= speed
        for i in range(len(bueiros)):
            bueiros[i].x -= speed
        if pegar == 0:
            carne.x -= speed
        if ini == 0 and pegar == 1:
            direcao = 0

    if pegar == 1 and ini != 0:
        direcao = -1

    if pegar == 0 and soltoucarne:
        direcao = 0

    return mimi


'''
 ######                                                                                                              
 #     #   ##    ####  #    #  ####  #####   ####  #    # #    # #####      ####   ####  #####   ####  #      #      
 #     #  #  #  #    # #   #  #    # #    # #    # #    # ##   # #    #    #      #    # #    # #    # #      #      
 ######  #    # #      ####   #      #    # #    # #    # # #  # #    #     ####  #      #    # #    # #      #      
 #     # ###### #      #  #   #  ### #####  #    # #    # #  # # #    #         # #      #####  #    # #      #      
 #     # #    # #    # #   #  #    # #   #  #    # #    # #   ## #    #    #    # #    # #   #  #    # #      #      
 ######  #    #  ####  #    #  ####  #    #  ####   ####  #    # #####      ####   ####  #    #  ####  ###### ###### 
'''


def scrolling(fundo, fundofrente, fundo2, fundo2frente):
    global pegar
    if not pegar:
        if fundo2.x <= 0 and fundo.x < fundo2.x:
            fundo.x = fundo2.x + fundo2.width
            fundofrente.x = fundo.x
        if fundo.x <= 0 and fundo2.x < fundo.x:
            fundo2.x = fundo.x + fundo.width
            fundo2frente.x = fundo2.x
    else:
        if fundo.x >= 0 and fundo2.x > fundo.x:
            fundo2.x = fundo.x - fundo2.width
            fundo2frente.x = fundo2.x
        if fundo2.x >= 0 and fundo.x > fundo2.x:
            fundo.x = fundo2.x - fundo.width
            fundofrente.x = fundo.x


'''
 ######                                                                          
 #     #  ####   ####     #    #  ####  #    # ###### #    # ###### #    # ##### 
 #     # #    # #    #    ##  ## #    # #    # #      ##  ## #      ##   #   #   
 #     # #    # #         # ## # #    # #    # #####  # ## # #####  # #  #   #   
 #     # #    # #  ###    #    # #    # #    # #      #    # #      #  # #   #   
 #     # #    # #    #    #    # #    #  #  #  #      #    # #      #   ##   #   
 ######   ####   ####     #    #  ####    ##   ###### #    # ###### #    #   #   
'''


def mov_cao(cao, lixeiras, speed):
    global olharcao
    for i in lixeiras:
        if cao.collided(i):
            if olharcao == -1:
                olharcao = 1
                aux = cao.x
                auy = cao.y
                cao = Sprite("images/dogesq.png", 8)
                cao.x = aux
                cao.y = auy
                cao.set_total_duration(1000)
            else:
                olharcao = -1
                aux = cao.x
                auy = cao.y
                cao = Sprite("images/dogdir.png", 8)
                cao.x = aux
                cao.y = auy
                cao.set_total_duration(1000)
    cao.x += speed*(-1)*olharcao

    return cao


'''
  #####                                                                          
 #     #   ##   #####     #    #  ####  #    # ###### #    # ###### #    # ##### 
 #        #  #  #    #    ##  ## #    # #    # #      ##  ## #      ##   #   #   
 #       #    # #    #    # ## # #    # #    # #####  # ## # #####  # #  #   #   
 #       ###### #####     #    # #    # #    # #      #    # #      #  # #   #   
 #     # #    # #   #     #    # #    #  #  #  #      #    # #      #   ##   #   
  #####  #    # #    #    #    #  ####    ##   ###### #    # ###### #    #   #   
'''


def mov_carro(carro, speed):
    carro.x -= 2*speed


'''

  #####                                                                     
 #     #   ##   #####      ####  #####  ######   ##   ##### #  ####  #    # 
 #        #  #  #    #    #    # #    # #       #  #    #   # #    # ##   # 
 #       #    # #    #    #      #    # #####  #    #   #   # #    # # #  # 
 #       ###### #####     #      #####  #      ######   #   # #    # #  # # 
 #     # #    # #   #     #    # #   #  #      #    #   #   # #    # #   ## 
  #####  #    # #    #     ####  #    # ###### #    #   #   #  ####  #    # 
'''



def cria_carro(janela, altura_rua):
    carros = ["images/carro.png", "images/carro2.png", "images/carro3.png", "images/carro4.png", "images/carro5.png"]
    carro = Sprite(choice(carros))
    carro.x = janela.width
    carro.y = altura_rua + 222
    return carro


'''
 #######                                                                                    
 #       #    # ###### #    # #   #     ####   ####  #      #      #  ####  #  ####  #    # 
 #       ##   # #      ##  ##  # #     #    # #    # #      #      # #      # #    # ##   # 
 #####   # #  # #####  # ## #   #      #      #    # #      #      #  ####  # #    # # #  # 
 #       #  # # #      #    #   #      #      #    # #      #      #      # # #    # #  # # 
 #       #   ## #      #    #   #      #    # #    # #      #      # #    # # #    # #   ## 
 ####### #    # ###### #    #   #       ####   ####  ###### ###### #  ####  #  ####  #    # 
 '''


def colisao(carros, caos, mimi, garrafas, dano, vidro, bark):
    global vidas, imune
    for carro in carros:
        if mimi.collided(carro):
            dano.play()
            vidas -= 1
            if vidas > 0:
                imune = True
                return True
    for cao in caos:
        if mimi.collided(cao):
                bark.play()
                dano.play()
                vidas -= 1
                if vidas > 0:
                    imune = True
                    return True
    for garrafa in garrafas:
        if mimi.collided(garrafa[0]):
            dano.play()
            garrafas.remove(garrafa)
            vidro.play()
            vidas -= 1
            if vidas > 0:
                imune = True
                return True
    return False


'''
 ######                                                                                        
 #     #  ####  ##### ##### #      ######     ####  #####  ######   ##   ##### #  ####  #    # 
 #     # #    #   #     #   #      #         #    # #    # #       #  #    #   # #    # ##   # 
 ######  #    #   #     #   #      #####     #      #    # #####  #    #   #   # #    # # #  # 
 #     # #    #   #     #   #      #         #      #####  #      ######   #   # #    # #  # # 
 #     # #    #   #     #   #      #         #    # #   #  #      #    #   #   # #    # #   ## 
 ######   ####    #     #   ###### ######     ####  #    # ###### #    #   #   #  ####  #    #                                                                                             
'''


def criagarrafa(bombardeiro, mimi):
    direc = -1
    if bombardeiro[0].x < mimi.x:
        direc = 1
    garrafa = Sprite("images/garrafa.png", 8)
    garrafa.x = bombardeiro[0].x
    garrafa.y = bombardeiro[0].y
    garrafa.set_total_duration(700)
    return [garrafa, direc, 2]


'''
 ######                                                                                             
 #     #  ####  ##### ##### #      ######    #    #  ####  #    # ###### #    # ###### #    # ##### 
 #     # #    #   #     #   #      #         ##  ## #    # #    # #      ##  ## #      ##   #   #   
 ######  #    #   #     #   #      #####     # ## # #    # #    # #####  # ## # #####  # #  #   #   
 #     # #    #   #     #   #      #         #    # #    # #    # #      #    # #      #  # #   #   
 #     # #    #   #     #   #      #         #    # #    #  #  #  #      #    # #      #   ##   #   
 ######   ####    #     #   ###### ######    #    #  ####    ##   ###### #    # ###### #    #   #   
'''


def mov_garrafa(garrafas, janela, vidro):
    global gravidade
    for garrafa in garrafas:
        garrafa[0].x += garrafa[1]*gravidade*janela.delta_time()
        if garrafa[0].y <= janela.height - 100:
            garrafa[0].y += 1/garrafa[2]*gravidade*janela.delta_time()
        else:
            garrafas.remove(garrafa)
            vidro.play()
        if garrafa[2] >= 0.1:
            garrafa[2] -= janela.delta_time()
    return garrafas


'''
  #####                                                                          
 #     # #       ####  #####    ##   #         #####  ######  ####  ###### ##### 
 #       #      #    # #    #  #  #  #         #    # #      #      #        #   
 #  #### #      #    # #####  #    # #         #    # #####   ####  #####    #   
 #     # #      #    # #    # ###### #         #####  #           # #        #   
 #     # #      #    # #    # #    # #         #   #  #      #    # #        #   
  #####  ######  ####  #####  #    # ######    #    # ######  ####  ######   #   
'''


def resetaglobais():
    global pulo, escalada, predio, andar, andaresq, pulei, olhar, chao, olharcao, invertecao, vidas, imune, invertefilhote, inverteu, ini, pegar, direcao, gravidade, olharpulo, soltoucarne, darksouls

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
    vidas = 7
    imune = False
    invertefilhote = 1
    inverteu = 0
    ini = 0
    pegar = 0
    direcao = 1
    olharpulo = 0
    soltoucarne = False
    darksouls = False

'''
 #######                                              
 #       #    # #####      ####    ##   #    # ###### 
 #       ##   # #    #    #    #  #  #  ##  ## #      
 #####   # #  # #    #    #      #    # # ## # #####  
 #       #  # # #    #    #  ### ###### #    # #      
 #       #   ## #    #    #    # #    # #    # #      
 ####### #    # #####      ####  #    # #    # ######                                                    
'''


def derrota():
    resetaglobais()
    return 4


def vitoria(janela, tempo):
    resetaglobais()
    ranking.appendranking(janela, tempo)
    return 0


'''
 #    #                                    
 #   #  # ##### ##### ###### #    #  ####  
 #  #   #   #     #   #      ##   # #      
 ###    #   #     #   #####  # #  #  ####  
 #  #   #   #     #   #      #  # #      # 
 #   #  #   #     #   #      #   ## #    # 
 #    # #   #     #   ###### #    #  ####                                          
'''


def mov_filhotes(filhotes):
    global ini
    for i in range(2):
        filhotes[i].x += filhotes[i+2]
        if filhotes[i].x > ini + 100:
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


'''
 #     #                                                                                 
 ##   ##   ##   #    # #    #  ####  #      ######     ####  #    #   ##   #    # ###### 
 # # # #  #  #  ##   # #    # #    # #      #         #      #    #  #  #  #   #  #      
 #  #  # #    # # #  # ###### #    # #      #####      ####  ###### #    # ####   #####  
 #     # ###### #  # # #    # #    # #      #              # #    # ###### #  #   #      
 #     # #    # #   ## #    # #    # #      #         #    # #    # #    # #   #  #      
 #     # #    # #    # #    #  ####  ###### ######     ####  #    # #    # #    # ###### 
'''


def tremebueiro(bueiro):
    aux = bueiro.x
    auy = bueiro.y
    bueiro = Sprite("images/bueirotreme.png", 8)
    bueiro.x = aux
    bueiro.y = auy
    bueiro.set_total_duration(250)

    return bueiro


'''
 #     #                                                                                               
 ##   ##   ##   #    # #    #  ####  #      ######    ###### #    # #####  #       ####  #####  ###### 
 # # # #  #  #  ##   # #    # #    # #      #         #       #  #  #    # #      #    # #    # #      
 #  #  # #    # # #  # ###### #    # #      #####     #####    ##   #    # #      #    # #    # #####  
 #     # ###### #  # # #    # #    # #      #         #        ##   #####  #      #    # #    # #      
 #     # #    # #   ## #    # #    # #      #         #       #  #  #      #      #    # #    # #      
 #     # #    # #    # #    #  ####  ###### ######    ###### #    # #      ######  ####  #####  ######                                                                                                     
'''


def explodebueiro(bueiro):
    aux = bueiro.x
    auy = bueiro.y
    bueiro = Sprite("images/bueiroegeiser.png", 11)
    bueiro.x = aux
    bueiro.y = auy - 135
    bueiro.set_total_duration(1000)

    return bueiro


'''
 #     #                                                                                                   
 ##   ##   ##   #    # #    #  ####  #      ######     ####   ####  #      #      #  ####  #  ####  #    # 
 # # # #  #  #  ##   # #    # #    # #      #         #    # #    # #      #      # #      # #    # ##   # 
 #  #  # #    # # #  # ###### #    # #      #####     #      #    # #      #      #  ####  # #    # # #  # 
 #     # ###### #  # # #    # #    # #      #         #      #    # #      #      #      # # #    # #  # # 
 #     # #    # #   ## #    # #    # #      #         #    # #    # #      #      # #    # # #    # #   ## 
 #     # #    # #    # #    #  ####  ###### ######     ####   ####  ###### ###### #  ####  #  ####  #    #                                                                                                         
'''


def colisao_bueiro(bueiros, mimi):
    global vidas, imune
    for bueiro in bueiros:
        if mimi.collided(bueiro):
                vidas -= 1
                if vidas >= 0:
                    imune = True
                    return True
    return False


'''
 #######                                                                                                     
    #    #    # #####   ####  #    # ###### #####     #    #  ####  #    # ###### #    # ###### #    # ##### 
    #    #    # #    # #    # #    # #      #    #    ##  ## #    # #    # #      ##  ## #      ##   #   #   
    #    ###### #    # #    # #    # #####  #    #    # ## # #    # #    # #####  # ## # #####  # #  #   #   
    #    #    # #####  #    # # ## # #      #####     #    # #    # #    # #      #    # #      #  # #   #   
    #    #    # #   #  #    # ##  ## #      #   #     #    # #    #  #  #  #      #    # #      #   ##   #   
    #    #    # #    #  ####  #    # ###### #    #    #    #  ####    ##   ###### #    # ###### #    #   #                                                                                                             
'''


def mov_bombardeiro(bombardeiros, mimi):
    for i in range(len(bombardeiros)):
        if bombardeiros[i][0].x < mimi.x and bombardeiros[i][1] == 0:
            aux = bombardeiros[i][0].x
            auy = bombardeiros[i][0].y
            bombardeiros[i][0] = Sprite("images/parado.png", 6)
            bombardeiros[i][0].set_total_duration(800)
            bombardeiros[i][0].x = aux
            bombardeiros[i][0].y = auy
            bombardeiros[i][1] = 1
        elif bombardeiros[i][0].x > mimi.x and bombardeiros[i][1] == 1:
            aux = bombardeiros[i][0].x
            auy = bombardeiros[i][0].y
            bombardeiros[i][0] = Sprite("images/bombard_esq.png", 6)
            bombardeiros[i][0].set_total_duration(800)
            bombardeiros[i][0].x = aux
            bombardeiros[i][0].y = auy
            bombardeiros[i][1] = 0


'''
 ######      ###    ##     ## ######## 
##    ##    ## ##   ###   ### ##       
##         ##   ##  #### #### ##       
##   #### ##     ## ## ### ## ######   
##    ##  ######### ##     ## ##       
##    ##  ##     ## ##     ## ##       
 ######   ##     ## ##     ## ########
'''


def jogo(janela):
    global pulo, chao, predio, imune, vidas, pegar, darksouls

    teclado = Window.get_keyboard()

    bombardeiro = [[Sprite("images/bombard_esq.png", 6), 0], [Sprite("images/bombard_esq.png", 6), 0], [Sprite("images/bombard_esq.png", 6), 0]]
    bombardeiro[0][0].set_total_duration(800)
    bombardeiro[1][0].set_total_duration(800)
    bombardeiro[2][0].set_total_duration(800)
    casa = Sprite("images/casa2.png")
    fundo = GameImage("images/fundoatras.png")
    fundofrente = GameImage("images/fundofrente.png")
    fundo2 = GameImage("images/fundoatras.png")
    fundo2frente = GameImage("images/fundofrente.png")
    mimi = Sprite("images/mimiparada.png", 1)
    cao = [Sprite("images/dogesq.png", 8), Sprite("images/dogesq.png", 8), Sprite("images/dogesq.png", 8)]
    carne = Sprite("images/chicken.png")
    lua = Sprite("images/lua.png")
    bueiros = [Sprite("images/bueiroparado.png", 1), Sprite("images/bueiroparado.png", 1), Sprite("images/bueiroparado.png", 1), Sprite("images/bueiroparado.png", 1), Sprite("images/bueiroparado.png", 1)]
    cao[0].set_total_duration(1000)
    cao[1].set_total_duration(1000)
    cao[2].set_total_duration(1000)
    mimi.set_total_duration(1000)
    static = [fundo, fundofrente, fundo2, fundo2frente]

    level = {
        0 : ["images/casa.png", 546],
        1 : ["images/casa3.png", 848],
        2 : ["images/casa2.png", 1204],
        3 : ["images/casa4.png", 1504],
        4 : ["images/casa2.png", 1938],
        5 : ["images/predio.png", 2275],
        6 : ["images/casa3.png", 2680],
        7 : ["images/predio.png", 3021],
        8 : ["images/casa4.png", 3393],
        9 : ["images/casa2.png", 3699],
        10 : ["images/casa.png", 4058],
        11 : ["images/casa3.png", 4458],
        12 : ["images/casa.png", 4822],
        13 : ["images/casa4.png", 5094],
        14 : ["images/predio.png", 5411],
        15 : ["images/casa.png", 5822],
        16 : ["images/casa2.png", 6211],
        17 : ["images/casa3.png", 6604],
        18 : ["images/predio.png", 6865],
        19 : ["images/casa2.png", 7341]
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

    garrafas = []

    for i in range(20):
        buildings.append(Sprite(level[i][0]))
        buildings[i].x = level[i][1]
        buildings[i].y = janela.height - 61 - buildings[i].height

    predio = buildings[0]
    chao = janela.height - 100
    carne.y = chao
    carne.x = 7350
    mimi.y = chao
    cao[0].y = janela.height - 108
    cao[1].y = janela.height - 108
    cao[2].y = janela.height - 108
    cao[0].x = 1600
    cao[1].x = 3500
    cao[2].x = 6300
    casa.y = altura_rua + 1

    bombardeiro[0][0].x = 2043
    bombardeiro[1][0].x = 3790
    bombardeiro[2][0].x = 6211 + buildings[2].width/2
    bombardeiro[0][0].y = buildings[2].y - bombardeiro[0][0].height
    bombardeiro[1][0].y = buildings[2].y - bombardeiro[0][0].height
    bombardeiro[2][0].y = buildings[2].y - bombardeiro[0][0].height

    lixeiras = [Sprite("images/lixeirainvertida.png"), Sprite("images/lixeira.png"), Sprite("images/lixeirainvertida.png"), Sprite("images/lixeira.png"), Sprite("images/lixeirainvertida.png"), Sprite("images/lixeira.png"), ]
    for i in range(len(lixeiras)):
        lixeiras[i].y = chao - lixeiras[i].height/2 + 5

    lixeiras[0].x = 1215 - 48
    lixeiras[1].x = 1774
    lixeiras[2].x = 3409 - 48
    lixeiras[3].x = 3910
    lixeiras[4].x = 6611 - 48
    lixeiras[5].x = 6046

    tempogarrafa = 0

    speed = 5
    lua.x = janela.width/2 - lua.width/2
    lua.y = 20

    tempo_car = 0
    rand_car = 10

    tempo_bueiro = 0
    tempo_geiser = 0
    parar_bueiro = 0
    rand_bueiro = uniform(3, 8)

    escondido = False
    gatescondido = False
    blink3 = blink4 = 0
    cont3 = cont4 = cont5 = 0
    blink = blink2 = 0
    cont2 = cont = 0

    exclamacao = Sprite("images/exclamacao.png")
    exclamacao.x = janela.width - exclamacao.width - 40
    exclamacao.y = janela.height - exclamacao.height - 40
    exclamacao.hide()

    carros = []

    filhotes = [(Sprite("images/filhoteesq.png", 6)), (Sprite("images/filhote.png", 6)), -1, 1]
    for i in range(2):
        filhotes[i].x = mimi.x + 50
        filhotes[i].y = mimi.y + 15
        filhotes[i].set_total_duration(1000)

    bueiros[0].x = 782
    bueiros[1].x = 2620
    bueiros[2].x = 3249
    bueiros[3].x = 4398
    bueiros[4].x = 7080
    for i in range(len(bueiros)):
        bueiros[i].y = mimi.y + 35
        bueiros[i].set_total_duration(250)

    esgoto = 0
    colidirbueiro = False

    '''
     #####                                                        
    #     # #####  ####  #####  #    #   ##   #####  ####  #    # 
    #         #   #    # #    # #    #  #  #    #   #    # #    # 
     #####    #   #    # #    # #    # #    #   #   #      ###### 
          #   #   #    # #####  # ## # ######   #   #      #    # 
    #     #   #   #    # #      ##  ## #    #   #   #    # #    # 
     #####    #    ####  #      #    # #    #   #    ####  #    #
    '''

    tempo = [(Sprite("images/yellow/meter_icon_holder_yellow.png")), (Sprite("images/yellow/timer.png"))]
    temp_bar_repete = [(Sprite("images/yellow/meter_bar_holder_center-repeating_yellow.png")),
                       (Sprite("images/yellow/meter_bar_holder_center-repeating_yellow.png")),
                       (Sprite("images/yellow/meter_bar_holder_center-repeating_yellow.png")),
                       (Sprite("images/yellow/meter_bar_holder_center-repeating_yellow.png")),
                       (Sprite("images/yellow/meter_bar_holder_center-repeating_yellow.png")),
                       (Sprite("images/yellow/meter_bar_holder_center-repeating_yellow.png"))]
    temp_repete = [(Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png")),
                   (Sprite("images/yellow/meter_bar_center-repeating_yellow.png"))]
    tempo_bar_dir = (Sprite("images/yellow/meter_bar_holder_right_edge_yellow.png"))
    tempo_dir = (Sprite("images/yellow/meter_bar_right_edge_yellow.png"))

    tempo[0].x = 5
    tempo[0].y = 5
    tempo[1].x = tempo[0].width/2 - tempo[1].width/2 + 5
    tempo[1].y = tempo[0].height/2 - tempo[1].height/2 + 5

    aux = 0
    aux += tempo[0].width - 10
    for barra in temp_repete:
        aux += barra.width
        barra.x = aux
        barra.y = 10
    tempo_dir.x = aux + temp_repete[0].width
    tempo_dir.y = 10
    aux = 0
    for barra in temp_bar_repete:
        aux += barra.width
        barra.x = aux
        barra.y = 10
    tempo_bar_dir.x = aux + temp_bar_repete[0].width
    tempo_bar_dir.y = 10

    cronometro = 0
    crono_1 = True
    segs = 5

    '''
    #     #
    #     # ######   ##   #      ##### #    #
    #     # #       #  #  #        #   #    #
    ####### #####  #    # #        #   ######
    #     # #      ###### #        #   #    #
    #     # #      #    # #        #   #    #
    #     # ###### #    # ######   #   #    #
    '''

    oneheart = GameImage("images/health/1heart.png")
    twohearts = GameImage("images/health/2hearts.png")
    threehearts = GameImage("images/health/3hearts.png")
    fourhearts = GameImage("images/health/4hearts.png")
    fivehearts = GameImage("images/health/5hearts.png")
    sixhearts = GameImage("images/health/6hearts.png")
    sevenhearts = GameImage("images/health/7hearts.png")

    oneheart.y = twohearts.y = threehearts.y = fourhearts.y = fivehearts.y = sixhearts.y = sevenhearts.y = 5
    oneheart.x = janela.width - oneheart.width - 5
    twohearts.x = janela.width - twohearts.width - 5
    threehearts.x = janela.width - threehearts.width - 5
    fourhearts.x = janela.width - fourhearts.width - 5
    fivehearts.x = janela.width - fivehearts.width - 5
    sixhearts.x = janela.width - sixhearts.width - 5
    sevenhearts.x = janela.width - sevenhearts.width - 5

    miado = Sound("sons/filhotes.ogg")
    miado.set_volume(10)
    miado.set_repeat(0)

    bark = Sound("sons/cao.ogg")
    bark.set_volume(15)
    bark.set_repeat(0)

    vrumm = Sound("sons/carro.ogg")
    vrumm.set_volume(10)
    vrumm.set_repeat(0)

    dano = Sound("sons/dano.ogg")
    dano.set_volume(40)
    dano.set_repeat(0)

    vidro = Sound("sons/vidro.ogg")
    vidro.set_volume(20)
    vidro.set_repeat(0)

    while True:

        if imune and darksouls:
            droparcarne(carne, mimi)
        if carne.y < janela.height - 100 and pegar == 0:
            carne.y += 1

        '''
        #     #                                         ######                         
        #  #  #   ##   #####  #    # # #    #  ####     #     # #      # #    # #    # 
        #  #  #  #  #  #    # ##   # # ##   # #    #    #     # #      # ##   # #   #  
        #  #  # #    # #    # # #  # # # #  # #         ######  #      # # #  # ####   
        #  #  # ###### #####  #  # # # #  # # #  ###    #     # #      # #  # # #  #   
        #  #  # #    # #   #  #   ## # #   ## #    #    #     # #      # #   ## #   #  
         ## ##  #    # #    # #    # # #    #  ####     ######  ###### # #    # #    # 
        '''
        
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
            vrumm.play()

        if blink > 0.2:
            exclamacao.hide()
            blink = blink2 = 0
            cont = 1
            escondido = False

        if cont == 1:
            blink2 += janela.delta_time()

        '''
        #     #               ######                         
        ##   ## # #    # #    #     # #      # #    # #    # 
        # # # # # ##  ## #    #     # #      # ##   # #   #  
        #  #  # # # ## # #    ######  #      # # #  # ####   
        #     # # #    # #    #     # #      # #  # # #  #   
        #     # # #    # #    #     # #      # #   ## #   #  
        #     # # #    # #    ######  ###### # #    # #    # 
        '''

        if gatescondido or blink3 > 0.2:
            mimi.hide()
            blink4 += janela.delta_time()
            cont3 = 0
            cont4 += janela.delta_time()
        if imune:
            cont5 += janela.delta_time()

        if cont4 >= 0.5:
            mimi.unhide()
            cont4 = 0
            blink3 = 0
            gatescondido = False

        if cont5 >= 3:
            cont5 = 0
            imune = False

        if blink4 > 0.2:
            mimi.unhide()
            blink4 = blink3 = 0
            cont3 = 1
            gatescondido = False

        if cont3 == 1:
            blink3 += janela.delta_time()

        ####################################

        scrolling(fundo, fundofrente, fundo2, fundo2frente)
        fundo.draw()
        fundo2.draw()
        lua.draw()
        fundofrente.draw()
        fundo2frente.draw()

        for i in range(len(buildings)):
            buildings[i].draw()

        for i in range(len(lixeiras)):
            lixeiras[i].draw()

        carne = pegarcarne(carne, mimi, janela)
        carne.draw()
        for i in range(len(cao)):
            if 0 - cao[i].width < cao[i].x < janela.width:
                cao[i].draw()
                cao[i].update()
                cao[i] = mov_cao(cao[i], lixeiras, speed)

        for pessoa in bombardeiro:
            if 0 < pessoa[0].x < janela.width:
                pessoa[0].draw()
                pessoa[0].update()

        mimi.draw()
        mimi.update()
        mimi = mov_mimi(mimi, teclado, speed, janela)
        mimi = escalar(mimi, teclado, buildings, janela)
        mimi = mov_cenario(mimi, teclado, static, bombardeiro, buildings, speed, janela, cao, carros, filhotes, carne, garrafas, bueiros, lixeiras)

        filhotes = mov_filhotes(filhotes)

        if 0 < filhotes[0].x < janela.width:
            miado.play()
        else:
            miado.stop()

        for i in range(2):
            filhotes[i].draw()
            filhotes[i].update()

        for bueiro in bueiros:
            bueiro.draw()
            bueiro.update()

        for carro in carros:
            carro.draw()
            mov_carro(carro, speed)
            if carro.x + carro.width < 0:
                carros.remove(carro)

        if imune is False:
            gatescondido = colisao(carros, cao, mimi, garrafas, dano, vidro, bark)

        topodopredio(mimi, janela)
        predioatual(mimi, buildings)

        tempo_bueiro += janela.delta_time()
        tempo_car += janela.delta_time()

        if tempo_bueiro >= rand_bueiro and esgoto == 0:
            for i in range(len(bueiros)):
                bueiros[i] = tremebueiro(bueiros[i])
            esgoto = 1

        if esgoto == 1:
            tempo_geiser += janela.delta_time()

        if tempo_geiser >= 1.5 and esgoto == 1:
            esgoto = 0
            rand_bueiro = 10000000
            for i in range(len(bueiros)):
                bueiros[i] = explodebueiro(bueiros[i])
            colidirbueiro = True
            tempo_geiser = 0

        if colidirbueiro is True:
            parar_bueiro += janela.delta_time()
            if imune is False:
                gatescondido = colisao_bueiro(bueiros, mimi)

        if parar_bueiro >= 1 and colidirbueiro is True:
            parar_bueiro = 0
            for i in range(len(bueiros)):
                aux = bueiros[i].x
                auy = bueiros[i].y
                bueiros[i] = Sprite("images/bueiroparado.png", 1)
                bueiros[i].x = aux
                bueiros[i].y = auy + 135
                bueiros[i].set_total_duration(1000)
            tempo_bueiro = 0
            rand_bueiro = uniform(3, 8)
            colidirbueiro = False

        if tempo_car >= rand_car:
            tempo_car = 0
            rand_car = uniform(4, 8)
            escondido = True

        for barra in temp_bar_repete:
            barra.draw()
        tempo_bar_dir.draw()
        for barra in temp_repete:
            barra.draw()
        tempo_dir.draw()

        for temp in tempo:
            temp.draw()

        cronometro += janela.delta_time()

        if cronometro >= segs:
            cronometro = 0
            segs = 2
            if crono_1 is True:
                tempo_dir.hide()
                crono_1 = False
            else:
                try:
                    temp_repete.pop(-1)
                except IndexError:
                    return derrota()

        for i in range(2):
            if mimi.collided(filhotes[i]) and pegar == 1:
                return vitoria(janela, len(temp_repete))
        if vidas == 0:
            return derrota()
        elif vidas == 1:
            oneheart.draw()
        elif vidas == 2:
            twohearts.draw()
        elif vidas == 3:
            threehearts.draw()
        elif vidas == 4:
            fourhearts.draw()
        elif vidas == 5:
            fivehearts.draw()
        elif vidas == 6:
            sixhearts.draw()
        elif vidas == 7:
            sevenhearts.draw()

        for garrafa in garrafas:
            garrafa[0].draw()
            garrafa[0].update()
        if tempogarrafa >= 1:
            tempogarrafa = 0
            for pessoa in bombardeiro:
                if 0 < pessoa[0].x < janela.width:
                    garrafas.append(criagarrafa(pessoa, mimi))

        garrafas = mov_garrafa(garrafas, janela, vidro)

        tempogarrafa += janela.delta_time()

        mov_bombardeiro(bombardeiro, mimi)

        if teclado.key_pressed("ESC"):
            resetaglobais()
            return 0

        exclamacao.draw()
        janela.update()

