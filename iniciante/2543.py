if __name__ == '__main__':
    while True:
        try:
            gameplays, identificador = map(int, input().split())
            jogos = 0
            for i in range(gameplays):
                identif, jogo = map(int, input().split())
                if identif == identificador and jogo == 0:
                    jogos += 1
            print(jogos)
        except EOFError:
            break