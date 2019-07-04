from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import uniform, choice

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
invertecao = 0
vidas = 7
imune = False
invertefilhote = 1
inverteu = 0
ini = 0
pegar = 0
direcao = 1

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
    global pulo, gravidade, andar, andaresq, pulei, olhar, direcao

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

        if teclado.key_pressed("RIGHT") and (mimi.x < janela.width/2 or (direcao == 0 and mimi.x + mimi.width < janela.width) or (direcao == -1 and mimi.x + mimi.width < janela.width)):
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

        if teclado.key_pressed("LEFT") and mimi.x >= 0 and (direcao != -1 or mimi.x > janela.width/2 + mimi.width):
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
    global pegar
    if mimi.collided(carne):
        pegar = 1
        carne.y = 40
        carne.x = janela.width - carne.height
    return carne


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
    for i in range(len(buildings)):
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

def mov_cenario(mimi, teclado, static, bombardeiro, buildings, speed, janela, cao, carros, filhotes, carne, garrafas):
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

        if pegar == 0:
            carne.x -= speed
        if buildings[16].x + buildings[16].width + 100 <= janela.width and pegar == 0:
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
        if pegar == 0:
            carne.x -= speed
        if ini == 0 and pegar == 1:
            direcao = 0

    if pegar == 1 and ini != 0:
        direcao = -1

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

def mov_cao(cao, janela, speed):
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
    else:
        olharcao *= -1
        invertecao = 1
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
def colisao(carros, caos, mimi, garrafas):
    global vidas, imune
    for carro in carros:
        if mimi.collided(carro):
            vidas -= 1
            if vidas > 0:
                imune = True
                return True
    for cao in caos:
        if mimi.collided(cao):
                vidas -= 1
                if vidas > 0:
                    imune = True
                    return True
    for garrafa in garrafas:
        if mimi.collided(garrafa[0]):
            garrafas.remove(garrafa)
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
    direcao = -1
    if bombardeiro[0].x < mimi.x:
        direcao = 1
    garrafa = Sprite("images/garrafa.png", 8)
    garrafa.x = bombardeiro[0].x
    garrafa.y = bombardeiro[0].y
    garrafa.set_total_duration(700)
    return [garrafa, direcao, 2]

'''
 ######                                                                                             
 #     #  ####  ##### ##### #      ######    #    #  ####  #    # ###### #    # ###### #    # ##### 
 #     # #    #   #     #   #      #         ##  ## #    # #    # #      ##  ## #      ##   #   #   
 ######  #    #   #     #   #      #####     # ## # #    # #    # #####  # ## # #####  # #  #   #   
 #     # #    #   #     #   #      #         #    # #    # #    # #      #    # #      #  # #   #   
 #     # #    #   #     #   #      #         #    # #    #  #  #  #      #    # #      #   ##   #   
 ######   ####    #     #   ###### ######    #    #  ####    ##   ###### #    # ###### #    #   #   
'''

def mov_garrafa(garrafas, janela):
    global gravidade
    for garrafa in garrafas:
        garrafa[0].x += garrafa[1]*gravidade*janela.delta_time()
        if garrafa[0].y <= janela.height - 100:
            garrafa[0].y += 1/garrafa[2]*gravidade*janela.delta_time()
        else:
            garrafas.remove(garrafa)
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
    global pulo, escalada, predio, andar, andaresq, pulei, olhar, chao, olharcao, invertecao, vidas, imune, invertefilhote, inverteu, ini, pegar, direcao

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
    return 0


def vitoria():
    resetaglobais()
    return 2


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
    global pulo, chao, predio, imune, vidas, pegar

    teclado = Window.get_keyboard()

    bombardeiro = [[Sprite("images/bombard_esq.png", 6), 0]]
    bombardeiro[0][0].set_total_duration(800)
    casa = Sprite("images/casa2.png")
    fundo = GameImage("images/fundoatras.png")
    fundofrente = GameImage("images/fundofrente.png")
    fundo2 = GameImage("images/fundoatras.png")
    fundo2frente = GameImage("images/fundofrente.png")
    mimi = Sprite("images/mimiparada.png", 1)
    cao = [Sprite("images/dogesq.png", 8)]
    carne = Sprite("images/chicken.png")
    lua = Sprite("images/lua.png")
    bueiros = [Sprite("images/bueiroparado.png", 1)]
    cao[0].set_total_duration(1000)
    mimi.set_total_duration(1000)
    static = [fundo, fundofrente, fundo2, fundo2frente]

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

    garrafas = []

    for i in range(17):
        buildings.append(Sprite(level[i][0]))
        buildings[i].x = level[i][1]
        buildings[i].y = janela.height - 61 - buildings[i].height

    predio = buildings[0]
    chao = janela.height - 100
    carne.y = chao
    carne.x = 7100
    mimi.y = chao
    cao[0].y = janela.height - 108
    cao[0].x += casa.width
    casa.y = altura_rua + 1
    bombardeiro[0][0].x = janela.width
    bombardeiro[0][0].y = 100
    tempogarrafa = 0

    speed = 5
    lua.x = janela.width/2 - lua.width/2
    lua.y = 20

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
    exclamacao.x = janela.width - exclamacao.width - 40
    exclamacao.y = janela.height - exclamacao.height - 40
    exclamacao.hide()

    carros = []

    filhotes = [(Sprite("images/filhoteesq.png", 6)), (Sprite("images/filhote.png", 6)), -1, 1]
    for i in range(2):
        filhotes[i].x = mimi.x + 50
        filhotes[i].y = mimi.y + 15
        filhotes[i].set_total_duration(1000)

    bueiros[0].x = mimi.x
    bueiros[0].y = mimi.y + 35
    bueiros[0].set_total_duration(250)
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

    while True:

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

        ####################################

        scrolling(fundo, fundofrente, fundo2, fundo2frente)
        fundo.draw()
        fundo2.draw()
        lua.draw()
        fundofrente.draw()
        fundo2frente.draw()

        for i in range(len(buildings)):
            buildings[i].draw()

        carne = pegarcarne(carne, mimi, janela)
        carne.draw()
        for i in range(len(cao)):
            cao[i].draw()
            cao[i].update()
            cao[i] = mov_cao(cao[i], janela, speed)

        bombardeiro[0][0].draw()
        bombardeiro[0][0].update()

        mimi.draw()
        mimi.update()
        mimi = mov_mimi(mimi, teclado, speed, janela)
        mimi = escalar(mimi, teclado, buildings, janela)
        mimi = mov_cenario(mimi, teclado, static, bombardeiro, buildings, speed, janela, cao, carros, filhotes, carne, garrafas)

        filhotes = mov_filhotes(filhotes)
        for i in range(2):
            filhotes[i].draw()
            filhotes[i].update()
        exclamacao.draw()

        for bueiro in bueiros:
            bueiro.draw()
            bueiro.update()

        for carro in carros:
            carro.draw()
            mov_carro(carro, speed)
            if carro.x + carro.width < 0:
                carros.remove(carro)

        if imune is False:
            gatescondido = colisao(carros, cao, mimi, garrafas)

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
            rand_car = uniform(2, 6)
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
                return vitoria()
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
                garrafas.append(criagarrafa(pessoa, mimi))

        garrafas = mov_garrafa(garrafas, janela)

        tempogarrafa += janela.delta_time()

        mov_bombardeiro(bombardeiro, mimi)

        janela.update()

