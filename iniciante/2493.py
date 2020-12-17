if __name__ == '__main__':
    while True:
        try:
            lista = []
            nomes = []
            entrada = int(input())
            for i in range(entrada):
                expressao = input().split()
                x = int(expressao[0])
                y = int(expressao[1].split('=')[0])
                z = int(expressao[1].split('=')[1])
                lista.append([x, y, z])
            for i in range(entrada):
                nome, indice, operacao = input().split()
                valores = lista[int(indice) - 1]
                x = valores[0]
                y = valores[1]
                z = valores[2]

                if operacao == '+':
                    if x + y != z:
                        nomes.append(nome)
                if operacao == '-':
                    if x - y != z:
                        nomes.append(nome)
                if operacao == '*':
                    if x * y != z:
                        nomes.append(nome)
                if operacao == 'I':
                    if x * y == z or x + y == z or x - y == z:
                        nomes.append(nome)
            if len(nomes) == 0:
                print('You Shall All Pass!')
            elif len(nomes) == entrada:
                print('None Shall Pass!')
            else:
                nomes.sort()
                print(' '.join(nomes))

        except EOFError:
            break
