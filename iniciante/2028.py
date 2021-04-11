if __name__ == '__main__':
    k = 0
    while True:
        k += 1
        try:
            vetor = ['0']
            entrada = int(input())
            for i in range(entrada + 1):
                for j in range(i):
                    vetor.append(str(i))
            if len(vetor) == 1:
                print(f'Caso {k}: 1 numero')
            else:
                print(f'Caso {k}: {len(vetor)} numeros')
            print(' '.join(vetor))
            print()
        except EOFError:
            break
