if __name__ == '__main__':
    certo = int(input())
    participantes = list(map(int, input().split()))
    print(participantes.count(certo))