if __name__ == '__main__':
    linha = input()
    while linha != '0':
        a, b, c = map(int, linha.split())

        area_casa = a * b
        area_real = (area_casa * 100) / c
        lado = int(area_real ** 0.5)

        print(lado)
        linha = input()
