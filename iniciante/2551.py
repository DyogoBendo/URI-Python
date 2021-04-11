if __name__ == '__main__':
    while True:
        try:
            treinos = int(input())
            media_anterior = 0
            for i in range(treinos):
                tempo, distancia = map(int, input().split())
                media = distancia / tempo
                if media > media_anterior:
                    print(i + 1)
                    media_anterior = media

        except EOFError:
            break