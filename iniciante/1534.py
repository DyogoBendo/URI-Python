def cria_matriz(matriz, ordem):
    repetiu = 0
    while ordem - repetiu > 0:
        for i in range(repetiu, ordem):
            for j in range(repetiu, ordem):
                if i == j == repetiu or i == j == ordem - 1:
                    matriz[i][j] = 1
                elif i == repetiu and j == ordem - 1:
                    matriz[i][j] = 2
                elif i == ordem - 1 and j == repetiu:
                    matriz[i][j] = 2
                if ordem - repetiu == 1:
                    matriz[i][j] = 2
        repetiu += 1
        ordem -= 1

    return matriz


if __name__ == '__main__':
    while True:
        try:
            ordem = int(input())
            if ordem == 0:
                break

            matriz = []

            for i in range(ordem):
                lista = []
                for j in range(ordem):
                    lista.append(3)
                matriz.append(lista)

            new_matrix = cria_matriz(matriz, ordem)

            for i in range(ordem):
                tx = ''
                for j in range(ordem):
                    tx += str(new_matrix[i][j])
                print(tx)
        except EOFError:
            break
