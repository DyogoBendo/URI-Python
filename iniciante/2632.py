def calcula_distancia (v, w):
    return (v['x'] - w['x'])**2 + (v['y'] - w['y'])**2


def coordenada_bate(c, v, w):
    l2 = calcula_distancia(v, w)
    if l2 == 0:
        return False
    t = ((c['x'] - v['x']) * (w['x'] - v['x']) + (c['y'] - v['y']) * (w['y'] - v['y'])) / l2
    answer = {
        'x': v['x'] + t * (w['x'] - v['x']),
        'y': v['y'] + t * (w['y'] - v['y'])
    }
    distancia = (calcula_distancia(c, answer)) ** 0.5
    if distancia <= raio:
        return True
    else:
        return False


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        w, h, yo, xo = map(int, input().split())
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

        ponto1 = {
            'x': xo,
            'y': yo
        }

        ponto2 = {
            'x': xo + w,
            'y': yo
        }

        ponto3 = {
            'x': xo,
            'y': yo + h
        }

        ponto4 = {
            'x': xo + w,
            'y': yo + h
        }

        if coordenada_bate(circulo, ponto1, ponto2) or coordenada_bate(circulo, ponto1, ponto3) or coordenada_bate(circulo, ponto2, ponto4) or coordenada_bate(circulo, ponto3, ponto4):
            print(dano)
        else:
            print(0)
