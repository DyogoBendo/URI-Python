if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            m, l = map(int, input().split())
            marcos = []
            leo = []
            for i in range(m):
                carta = list(map(int, input().split()))
                marcos.append(carta)
            for i in range(l):
                carta = list(map(int, input().split()))
                leo.append(carta)
            pos_marcos, pos_leo = map(int, input().split())
            carta_marcos = marcos[pos_marcos - 1]
            carta_leo = leo[pos_leo - 1]
            atributo = int(input())

            if carta_marcos[atributo - 1] > carta_leo[atributo - 1]:
                print('Marcos')
            elif carta_marcos[atributo - 1] < carta_leo[atributo - 1]:
                print('Leonardo')
            else:
                print('Empate')


        except EOFError:
            break
