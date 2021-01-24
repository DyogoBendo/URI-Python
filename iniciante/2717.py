if __name__ == '__main__':
    expediente = int(input())
    presente1, presente2 = map(int, input().split())
    if expediente >= presente1 + presente2:
        print('Farei hoje!')
    else:
        print('Deixa para amanha!')
