if __name__ == '__main__':
    entrada = list(map(int, input().split()))
    total = sum(entrada)
    posicao = (total % 9)
    renas = ['Rudolph', 'Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen']

    print(renas[posicao])
