def cria_matriz(matriz, ordem):
    ordem_original = ordem
    repetiu = 0
    while ordem - repetiu > 0:
        for i in range(repetiu, ordem):
            for j in range(repetiu, ordem):
                if i == repetiu:
                    matriz[i][j] = j + 1 - repetiu
                elif j == repetiu:
                    matriz[i][j] = i + 1 - repetiu
                elif i == ordem_original - 1:
                    matriz[i][j] = ordem_original - j
                elif j == ordem_original - 1:
                    matriz[i][j] = ordem_original - i
        repetiu += 1
        ordem -= 1
        ordem_original -= 1

    return matriz


if __name__ == '__main__':
    while True:
        ordem = int(input())
        if ordem == 0:
            break

        matriz = []

        for i in range(ordem):
            lista = []
            for j in range(ordem):
                lista.append(1)
            matriz.append(lista)

        new_matrix = cria_matriz(matriz, ordem)

        for i in range(ordem):
            tx = ''
            for j in range(ordem):
                tx += " %3d" % new_matrix[i][j]
            print(tx[1:])
        print("")

