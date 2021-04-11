def testa_triangulo(a, b, c):
    if abs(b - c) >= a or a >= b + c:
        return False
    if abs(a - c) >= b or b >= a + c:
        return False
    if abs(b - a) >= c or c >= a + b:
        return False
    return True


if __name__ == '__main__':
    lista = list(map(int, input().split()))
    lista.sort()
    teste = testa_triangulo(lista[0], lista[1], lista[2])
    if teste:
        print('S')
    else:
        teste = testa_triangulo(lista[1], lista[2], lista[3])
        if teste:
            print('S')
        else:
            print('N')


