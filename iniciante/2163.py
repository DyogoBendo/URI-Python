def procura_sabe(matriz, linhas, colunas):
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == 42:
                if 0 < i < linhas - 1 and 0 < j < colunas - 1:
                    if matriz[i + 1][j] == 7 \
                            and matriz[i - 1][j] == 7 \
                            and matriz[i][j + 1] == 7 \
                            and matriz[i][j - 1] == 7 \
                            and matriz[i - 1][j - 1] == 7 \
                            and matriz[i - 1][j + 1] == 7 \
                            and matriz[i + 1][j - 1] == 7 \
                            and matriz[i + 1][j + 1] == 7:
                        return [i + 1, j + 1]
    return [0, 0]


if __name__ == '__main__':
    linhas, colunas = map(int, input().split())
    matriz = []
    for i in range(linhas):
        vetor = list(map(int, input().split()))
        matriz.append(vetor)
    print(' '.join(map(str, procura_sabe(matriz, linhas, colunas))))