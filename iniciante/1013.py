# -*- coding: utf-8 -*-
def maior(a, b):
    return (a + b + abs(a - b)) / 2


if __name__ == '__main__':
    linha = input().split()
    resultado = int(linha[0])
    for teste in linha:
        resultado = maior(resultado, int(teste))

    print(f"{resultado:.0f} eh o maior")
