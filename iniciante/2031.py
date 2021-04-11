def define_ganhador(j1, j2):
    if j1 == 'ataque':
        if j2 == 'ataque':
            print('Aniquilacao mutua')
        else:
            print('Jogador 1 venceu')
    elif j1 == 'pedra':
        if j2 == 'pedra':
            print('Sem ganhador')
        elif j2 == 'papel':
            print('Jogador 1 venceu')
        else:
            print('Jogador 2 venceu')
    else:
        if j2 == 'papel':
            print('Ambos venceram')
        else:
            print('Jogador 2 venceu')


if __name__ == '__main__':
    repete = int(input())
    for i in range(repete):
        e1 = input()
        e2 = input()
        define_ganhador(e1, e2)
