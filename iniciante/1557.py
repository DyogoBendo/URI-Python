def cria_matriz(matriz, ordem):
    for i in range(0, ordem):
        for j in range(0, ordem):
            matriz[i][j] = 2 ** (i + j)
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

        ultimo_numero = new_matrix[ordem - 1][ordem - 1]
        ultimo_numero = str(ultimo_numero)

        for i in range(ordem):
            tx = ''
            for j in range(ordem):
                tx += f" %{len(ultimo_numero)}d" % new_matrix[i][j]
            print(tx[1:])
        print("")

