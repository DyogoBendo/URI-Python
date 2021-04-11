if __name__ == '__main__':
    p, j1, j2, r, a = map(int, input().split())
    if a == 1:
        if r == 0:
            print('Jogador 1 ganha!')
        else:
            print('Jogador 2 ganha!')
    else:
        if r == 0:
            resultado = j1 + j2
            if resultado % 2 == 0:
                if p == 1:
                    print('Jogador 1 ganha!')
                else:
                    print('Jogador 2 ganha!')
            else:
                if p == 0:
                    print('Jogador 1 ganha!')
                else:
                    print('Jogador 2 ganha!')
        else:
            print('Jogador 1 ganha!')