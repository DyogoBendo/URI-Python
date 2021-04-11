if __name__ == '__main__':
    while True:
        try:
            n, m = map(int, input().split())
            matriz = []
            for i in range(n):
                vetor = list(map(int, input().split()))
                matriz.append(vetor)
            for i in range(n):
                for j in range(m):
                    conta = 0
                    if matriz[i][j] == 1:
                        matriz[i][j] = 9
                    else:
                        if i + 1 < n:
                            if matriz[i + 1][j] == 1:
                                conta += 1
                        if i > 0:
                            if matriz[i - 1][j] == 9:
                                conta += 1
                        if j + 1 < m:
                            if matriz[i][j + 1] == 1:
                                conta += 1
                        if j > 0:
                            if matriz[i][j - 1] == 9:
                                conta += 1
                        matriz[i][j] = conta
            for i in range(n):
                resultado = ''.join(map(str, matriz[i]))
                print(resultado)

        except EOFError:
            break
