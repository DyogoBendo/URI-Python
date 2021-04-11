if __name__ == '__main__':
    pesquisadas = int(input())
    palavras = []
    for i in range(pesquisadas):
        palavras.append(input())

    pesquisas = int(input())
    for i in range(pesquisas):
        num = 0
        grande = 0
        inicio = input()
        for palavra in palavras:
            teste = ''
            if palavra.startswith(inicio):
               num += 1
               if len(palavra) > grande:
                   grande = len(palavra)
        if grande == 0:
            print(-1)
        else:
            print(f'{num} {grande}')
