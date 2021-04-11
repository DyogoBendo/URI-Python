def define_vencedor(dabriel, guarte, bonus):
    golpe_dabriel = (dabriel[0] + dabriel[1]) / 2
    golpe_guarte = (guarte[0] + guarte[1]) / 2

    if dabriel[2] % 2 == 0:
        golpe_dabriel += bonus
    if guarte[2] % 2 == 0:
        golpe_guarte += bonus

    if golpe_dabriel > golpe_guarte:
        print('Dabriel')
    elif golpe_guarte == golpe_dabriel:
        print('Empate')
    else:
        print('Guarte')


if __name__ == '__main__':
    repete = int(input())
    for i in range(repete):
        bonus = int(input())
        dabriel = list(map(int, input().split()))
        guarte = list(map(int, input().split()))
        define_vencedor(dabriel, guarte, bonus)