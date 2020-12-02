if __name__ == '__main__':
    while True:
        ordem = int(input())
        if ordem == 0:
            break

        matriz_original = []
        repetiu = 0

        while ordem - repetiu > 0:
            for i in range(repetiu, ordem):
                vetor = []
                for j in range(repetiu, ordem):
                    if repetiu == 0:
                        vetor.append(1)
                    else:
                        matriz_original[i][j] = repetiu + 1
                if repetiu == 0:
                    matriz_original.append(vetor)
            repetiu += 1
            ordem -= 1
        for numeros in matriz_original:
            linha = '   '.join(map(str, numeros))
            print("  " + linha)
        ordem += 1
        if ordem != 0:
            print("")
