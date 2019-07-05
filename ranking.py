from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import uniform, choice

pressionado = 0

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


def appendranking(janela, tempo):
    global pressionado
    mouse = Window.get_mouse()
    rank = open("ranking.txt", "a+")

    a = Sprite("images/keyboard/a.png")
    b = Sprite("images/keyboard/b.png")
    c = Sprite("images/keyboard/c.png")
    d = Sprite("images/keyboard/d.png")
    e = Sprite("images/keyboard/e.png")
    f = Sprite("images/keyboard/f.png")
    g = Sprite("images/keyboard/g.png")
    h = Sprite("images/keyboard/h.png")
    i = Sprite("images/keyboard/i.png")
    j = Sprite("images/keyboard/j.png")
    k = Sprite("images/keyboard/k.png")
    l = Sprite("images/keyboard/l.png")
    m = Sprite("images/keyboard/m.png")
    n = Sprite("images/keyboard/n.png")
    o = Sprite("images/keyboard/o.png")
    p = Sprite("images/keyboard/p.png")
    q = Sprite("images/keyboard/q.png")
    r = Sprite("images/keyboard/r.png")
    s = Sprite("images/keyboard/s.png")
    t = Sprite("images/keyboard/t.png")
    u = Sprite("images/keyboard/u.png")
    v = Sprite("images/keyboard/v.png")
    w = Sprite("images/keyboard/w.png")
    x = Sprite("images/keyboard/x.png")
    y = Sprite("images/keyboard/y.png")
    z = Sprite("images/keyboard/z.png")
    enter = Sprite("images/keyboard/enter.png")
    space = Sprite("images/keyboard/space.png")

    lua = Sprite("images/lua.png")
    lua.x = janela.width/2 - lua.width/2
    lua.y = 20

    fundo = GameImage("images/fundoatras.png")
    fundofrente = GameImage("images/fundofrente.png")
    fundo2 = GameImage("images/fundoatras.png")
    fundo2frente = GameImage("images/fundofrente.png")
    fundo.x = fundofrente.x = 0
    fundo.y = fundofrente.y = fundo2.y = fundo2frente.y = -215
    fundo2.x = fundo2frente.x = fundo.width
    static = [fundo, fundofrente, fundo2, fundo2frente]

    q.y = janela.height/2
    w.y = janela.height/2
    e.y = janela.height/2
    r.y = janela.height/2
    t.y = janela.height/2
    y.y = janela.height/2
    u.y = janela.height/2
    i.y = janela.height/2
    o.y = janela.height/2
    p.y = janela.height/2
    q.x = janela.width/4
    w.x += q.x + q.width
    e.x += w.x + q.width
    r.x += e.x + q.width
    t.x += r.x + q.width
    y.x += t.x + q.width
    u.x += y.x + q.width
    i.x += u.x + q.width
    o.x += i.x + q.width
    p.x += o.x + q.width
    a.y = janela.height/2 + q.height
    s.y = janela.height/2 + q.height
    d.y = janela.height/2 + q.height
    f.y = janela.height/2 + q.height
    g.y = janela.height/2 + q.height
    h.y = janela.height/2 + q.height
    j.y = janela.height/2 + q.height
    k.y = janela.height/2 + q.height
    l.y = janela.height/2 + q.height
    a.x += janela.width/4 + q.width/2
    s.x += a.x + q.width
    d.x += s.x + q.width
    f.x += d.x + q.width
    g.x += f.x + q.width
    h.x += g.x + q.width
    j.x += h.x + q.width
    k.x += j.x + q.width
    l.x += k.x + q.width
    z.y = janela.height/2 + a.height*2
    x.y = janela.height/2 + a.height*2
    c.y = janela.height/2 + a.height*2
    v.y = janela.height/2 + a.height*2
    b.y = janela.height/2 + a.height*2
    n.y = janela.height/2 + a.height*2
    m.y = janela.height/2 + a.height*2
    z.x += janela.width/4 + q.width + 20
    x.x += z.x + q.width
    c.x += x.x + q.width
    v.x += c.x + q.width
    b.x += v.x + q.width
    n.x += b.x + q.width
    m.x += n.x + q.width

    enter.x = l.x + q.width + 50
    enter.y = janela.height/2 + a.height
    space.y = janela.height/3 + a.height*5
    space.x = janela.width/3 + q.width/3
    string = ''

    while True:
        scrolling(fundo, fundofrente, fundo2, fundo2frente, static)
        fundo.draw()
        fundo2.draw()
        lua.draw()
        fundofrente.draw()
        fundo2frente.draw()

        enter.draw()
        space.draw()

        q.draw()
        w.draw()
        e.draw()
        r.draw()
        t.draw()
        y.draw()
        u.draw()
        i.draw()
        o.draw()
        p.draw()
        a.draw()
        s.draw()
        d.draw()
        f.draw()
        g.draw()
        h.draw()
        j.draw()
        k.draw()
        l.draw()
        z.draw()
        x.draw()
        c.draw()
        v.draw()
        b.draw()
        n.draw()
        m.draw()

        if mouse.is_over_object(q) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'Q'
            pressionado = 1
        if mouse.is_over_object(w) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'W'
            pressionado = 1
        if mouse.is_over_object(e) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'E'
            pressionado = 1
        if mouse.is_over_object(r) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'R'
            pressionado = 1
        if mouse.is_over_object(t) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'T'
            pressionado = 1
        if mouse.is_over_object(y) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'Y'
            pressionado = 1
        if mouse.is_over_object(u) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'U'
            pressionado = 1
        if mouse.is_over_object(i) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'I'
            pressionado = 1
        if mouse.is_over_object(o) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'O'
            pressionado = 1
        if mouse.is_over_object(p) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'P'
            pressionado = 1
        if mouse.is_over_object(a) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'A'
            pressionado = 1
        if mouse.is_over_object(s) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'S'
            pressionado = 1
        if mouse.is_over_object(d) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'D'
            pressionado = 1
        if mouse.is_over_object(f) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'F'
            pressionado = 1
        if mouse.is_over_object(g) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'G'
            pressionado = 1
        if mouse.is_over_object(h) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'H'
            pressionado = 1
        if mouse.is_over_object(j) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'J'
            pressionado = 1
        if mouse.is_over_object(k) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'K'
            pressionado = 1
        if mouse.is_over_object(l) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'L'
            pressionado = 1
        if mouse.is_over_object(z) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'Z'
            pressionado = 1
        if mouse.is_over_object(x) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'X'
            pressionado = 1
        if mouse.is_over_object(c) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'C'
            pressionado = 1
        if mouse.is_over_object(v) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'V'
            pressionado = 1
        if mouse.is_over_object(b) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'B'
            pressionado = 1
        if mouse.is_over_object(n) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'N'
            pressionado = 1
        if mouse.is_over_object(m) and mouse.is_button_pressed(1) and pressionado == 0:
            string += 'M'
            pressionado = 1
        if mouse.is_over_object(space) and mouse.is_button_pressed(1) and pressionado == 0:
            string += ' '
            pressionado = 1
        if mouse.is_over_object(enter) and mouse.is_button_pressed(1) and pressionado == 0:
            rank.write(string + "$" + str(62-tempo) + "\n")
            rank.close()
            sort()
            ranking(janela)
            return 0
        if not mouse.is_button_pressed(1):
            pressionado = 0

        janela.draw_text(string, janela.width/3, janela.height/4, size=35, color=(255, 255, 255), bold=True)
        janela.update()


def sort():
    rank = open("ranking.txt", "r")

    l = rank.readlines()
    for i in range(len(l)):
        l[i] = l[i].split('$')

    l.sort(key=lambda a: int(a[1]), reverse=False)

    for i in range(len(l)):
        l[i] = l[i][0] + "$" + l[i][1]

    rank.close()
    rank = open("ranking.txt", "w")
    if len(l) >= 5:
        for i in range(5):
            rank.write(l[i])
    else:
        for i in range(len(l)):
            rank.write(l[i])
    rank.close()


def ranking(janela):
    teclado = Window.get_keyboard()

    lua = Sprite("images/lua.png")
    lua.x = janela.width/2 - lua.width/2
    lua.y = 20

    fundo = GameImage("images/fundoatras.png")
    fundofrente = GameImage("images/fundofrente.png")
    fundo2 = GameImage("images/fundoatras.png")
    fundo2frente = GameImage("images/fundofrente.png")
    fundo.x = fundofrente.x = 0
    fundo.y = fundofrente.y = fundo2.y = fundo2frente.y = -215
    fundo2.x = fundo2frente.x = fundo.width
    static = [fundo, fundofrente, fundo2, fundo2frente]

    letrinhas = GameImage("images/menu/letrinhas.png")
    letrinhas.x = 30
    letrinhas.y = 30


    f = open("ranking.txt", "r+")
    l = f.readlines()

    while True:
        scrolling(fundo, fundofrente, fundo2, fundo2frente, static)
        fundo.draw()
        fundo2.draw()
        lua.draw()
        fundofrente.draw()
        fundo2frente.draw()

        letrinhas.draw()

        y = 60 + 80
        for i in l:
            i = i.split("$")
            j = ''
            for _ in i[1][:-1]:
                j += _
            j += " s"

            janela.draw_text(i[0], 30, y, size=35, color=(255, 255, 255), bold=True)
            janela.draw_text(j, 320, y, size=40, color=(255, 255, 255), bold=True)
            y += 50
        if teclado.key_pressed("ESC"):
            f.close()
            return 0

        janela.update()
