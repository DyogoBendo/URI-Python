# -*- coding: utf-8 -*-


def triangulo(a, c):
    area = a * c / 2
    print(f"TRIANGULO: {area:.3f}")


def circulo(c):
    area = c ** 2 * 3.14159
    print(f"CIRCULO: {area:.3f}")


def trapezio(a, b, c):
    area = ((a + b) * c) / 2
    print(f"TRAPEZIO: {area:.3f}")


def quadrado(b):
    area = b ** 2
    print(f"QUADRADO: {area:.3f}")


def retangulo(a, b):
    area = a * b
    print(f"RETANGULO: {area:.3f}")


if __name__ == '__main__':
    linha = input().split()
    a = float(linha[0])
    b = float(linha[1])
    c = float(linha[2])

    triangulo(a, c)
    circulo(c)
    trapezio(a, b, c)
    quadrado(b)
    retangulo(a, b)
