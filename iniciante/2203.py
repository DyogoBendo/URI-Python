if __name__ == '__main__':
    while True:
        try:
            xf, yf, xi, yi, v, r1, r2 = map(int, input().split())
            distancia = ((xf - xi) ** 2 + (yf - yi) ** 2) ** 0.5
            distancia_percorrida = 1.5 * v
            if distancia_percorrida + distancia > r1 + r2:
                print('N')
            else:
                print('Y')
        except EOFError:
            break