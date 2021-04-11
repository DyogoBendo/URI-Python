from math import log

if __name__ == '__main__':
    n = int(input())
    calculo_minimo = n / log(n)
    calculo_maximo = 1.25506 * calculo_minimo

    print(f'{calculo_minimo:.1f} {calculo_maximo:.1f}')