if __name__ == '__main__':
    repete = int(input())
    for i in range(repete):
        jogador1, escolha1, jogador2, escolha2 = input().split()
        acao1, acao2 = map(int, input().split())
        resultado = acao1 + acao2
        if resultado % 2 == 0:
            if escolha1 == 'PAR':
                print(jogador1)
            else:
                print(jogador2)
        else:
            if escolha1 == 'IMPAR':
                print(jogador1)
            else:
                print(jogador2)
