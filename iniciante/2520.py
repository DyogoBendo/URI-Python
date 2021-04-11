if __name__ == '__main__':
    while True:
        try:
            n, m = map(int, input().split())
            matriz = []
            posicao_pokemon = []
            posicao_pessoa = []
            for i in range(n):
                vetor = list(map(int, input().split()))
                try:
                    posicao_pessoa = [i, vetor.index(1)]
                except:
                    pass
                try:
                    posicao_pokemon = [i, vetor.index(2)]
                except:
                    pass
                matriz.append(vetor)

            distancia = abs(posicao_pessoa[0] - posicao_pokemon[0]) + abs(posicao_pokemon[1] - posicao_pessoa[1])
            print(distancia)

        except EOFError:
            break