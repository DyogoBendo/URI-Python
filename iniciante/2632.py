def calcula_equacao(xo, c):
    a = 1
    b = 2 * xo
    c -= xo ** 2

    delta = (b ** 2 - (4 * a * c))
    if delta < 0:
        return None
    else:
        x1 = (-b + (delta ** 0.5)) / 2
        x2 = (-b - (delta ** 0.5)) / 2
        return [x1, x2]


def calcula_coordenada(r, s, t, u, circulo):
    eixo_x_baixo = abs(s - circulo['x'])
    eixo_x_cima = abs(t - circulo['x'])

    eixo_y_baixo = abs(r - circulo['y'])
    eixo_y_cima = abs(u - circulo['y'])

    eixo_y_menor = eixo_y_baixo if eixo_y_baixo < eixo_y_cima else eixo_y_cima
    eixo_x_menor = eixo_x_baixo if eixo_x_baixo < eixo_x_cima else eixo_x_cima

    c = circulo["raio"] ** 2 - eixo_y_menor ** 2
    resultado = calcula_equacao(circulo["x"], c)

    print(resultado)
    if resultado:
        cima, baixo = resultado
        if baixo >= eixo_x_menor:
            return True

    c = circulo["raio"] ** 2 - eixo_x_menor ** 2
    resultado = calcula_equacao(circulo["y"], c)
    print(resultado)
    if resultado:
        cima, baixo = resultado
        if baixo >= eixo_y_menor:
            return True
    return False


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        w, h, xo, yo = map(int, input().split())
        are_commum = False
        magia, nivel, cx, cy = input().split()
        cx, cy = map(int, [cx, cy])
        if magia == 'fire':
            if nivel == '1':
                raio = 20
            elif nivel == '2':
                raio = 30
            else:
                raio = 50
            dano = 200
        elif magia == 'water':
            if nivel == '1':
                raio = 10
            elif nivel == '2':
                raio = 25
            else:
                raio = 40
            dano = 300
        elif magia == 'earth':
            if nivel == '1':
                raio = 25
            elif nivel == '2':
                raio = 55
            else:
                raio = 70
            dano = 400
        else:
            if nivel == '1':
                raio = 18
            elif nivel == '2':
                raio = 38
            else:
                raio = 60
            dano = 100

        circulo = {
            'x': cx,
            'y': cy,
            'raio': raio
        }
        r = yo
        s = xo
        t = xo + w
        u = yo + h

        if calcula_coordenada(r, s, t, u, circulo):
            print(dano)
        else:
            print(0)
