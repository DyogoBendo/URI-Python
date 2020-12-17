if __name__ == '__main__':
    valores = list(map(int, input().split()))
    valores.sort()
    if valores[0] + valores [1] <= valores[2]:
        print('Invalido')
    else:
        if valores.count(valores[0]) == 3:
            print('Valido-Equilatero')
        elif valores.count(valores[0]) == 2:
            print('Valido-Isoceles')
        elif valores.count(valores[1]) == 2:
            print('Valido-Isoceles')
        else:
            print('Valido-Escaleno')

        if valores[0] ** 2 + valores[1] ** 2 == valores[2] ** 2:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
