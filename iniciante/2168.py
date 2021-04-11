if __name__ == '__main__':
    repete = int(input())
    matriz = []
    for i in range(repete + 1):
        vetor = list(map(int, input().split()))
        matriz.append(vetor)
    for i in range(repete):
        resposta = ''
        for j in range(repete):
            super_esq = matriz[i][j]
            super_dir = matriz [i][j + 1]
            infer_esq = matriz[i + 1][j]
            infer_dir = matriz[i + 1][j + 1]
            if super_dir + super_esq + infer_dir + infer_esq > 1:
                resposta += 'S'
            else:
                resposta += 'U'
        print(resposta)