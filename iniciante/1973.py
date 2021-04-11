if __name__ == '__main__':
    num_estrelas = int(input())
    estrelas = list(map(int, input().split()))

    fazendas_visitadas = [0] * num_estrelas

    i = 0
    while True:
        if i == 0 and estrelas[i] % 2 == 0:
            fazendas_visitadas[i] = 1
            if estrelas[i] > 0:
                estrelas[i] -= 1
            break
        if i == num_estrelas - 1 and estrelas[i] % 2 != 0:
            fazendas_visitadas[i] = 0
            if estrelas[i] > 0:
                estrelas[i] -= 1
            break
        elif estrelas[i] % 2 == 0:
            fazendas_visitadas[i] = 1
            if estrelas[i] > 0:
                estrelas[i] -= 1
            i -= 1
        elif estrelas[i] % 2 != 0:
            fazendas_visitadas[i] = 1
            estrelas[i] -= 1
            i += 1

    print(f'{sum(fazendas_visitadas)} {sum(estrelas)}')
