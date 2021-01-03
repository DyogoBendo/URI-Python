def coordenada_bate(retangulo, circulo, raio):
    distancia = (((retangulo[0] - circulo[0]) ** 2) + ((retangulo[1] - circulo[1]) ** 2)) ** 0.5
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

        esquerda_cima = xo, yo + h
        esquerda_baixo = xo, yo
        direita_cima = xo + h, yo + h
        direita_baixo = xo + h, yo
        circulo = int(cx), int(cy)

        if coordenada_bate(esquerda_cima, circulo, raio) or coordenada_bate(esquerda_baixo, circulo, raio) \
                or coordenada_bate(direita_baixo, circulo, raio) or coordenada_bate(direita_cima, circulo, raio):
            print(dano)
        else:
            print(0)
