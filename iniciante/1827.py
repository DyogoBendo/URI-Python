def cria_matriz(matriz, ordem):
    interior = ordem // 3
    meio = ordem // 2
    for i in range(ordem):
        for j in range(ordem):
            if j == i:
                matriz [i][j] = 2
            if i + j == ordem - 1:
                matriz [i][j] = 3

            if i >= interior <= j <= ordem - interior - 1 >= i:
                matriz[i][j] = 1
            if i == meio == j:
                matriz[i][j] = 4

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
                    lista.append(0)
                matriz.append(lista)

            new_matrix = cria_matriz(matriz, ordem)

            for i in range(ordem):
                tx = ''
                for j in range(ordem):
                    tx += str(new_matrix[i][j])
                print(tx)
            print()
        except EOFError:
            break
