def testa_altura(altura_canos, altura_sapo):
    for i in range(canos - 1):
        cano_inicial = altura_canos[i]
        proximo_cano = altura_canos[i + 1]
        if abs(proximo_cano - cano_inicial) > altura_sapo:
            print('GAME OVER')
            return
    print('YOU WIN')


if __name__ == '__main__':
    altura_sapo, canos = map(int, input().split())
    altura_canos = list(map(int, input().split()))

    testa_altura(altura_canos, altura_sapo)