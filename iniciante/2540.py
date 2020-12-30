if __name__ == '__main__':
    while True:
        try:
            a = int(input())
            votos = list(map(int, input().split()))
            num_1 = votos.count(1)
            if num_1 / a >= 2/3:
                print('impeachment')
            else:
                print('acusacao arquivada')
        except EOFError:
            break