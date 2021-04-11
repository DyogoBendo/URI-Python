if __name__ == '__main__':
    while True:
        try:
            inicio = ord('a') - 1
            linhas = int(input())
            for l in range(linhas):
                entrada = input().split()
                total = 0
                for i in range(len(entrada)):
                    tamanho = len(entrada[i])
                    if i > 0:
                        total += 3 - tamanho
                    total += tamanho
                print(chr(inicio + total))
        except EOFError:
            break
