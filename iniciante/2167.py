def verifica_queda(numeros):
    for i in range(1, len(numeros)):
        anterior = numeros[i - 1]
        atual = numeros [i]

        if atual < anterior:
            return i + 1
    return 0


if __name__ == '__main__':
    repete = int(input())
    entrada = list(map(int, input().split()))
    print(verifica_queda(entrada))
