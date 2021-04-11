if __name__ == '__main__':
    k = 0
    while True:
        k += 1
        try:
            e1 = int(input())
            e1 = str(e1)
            e2 = input()
            print(f'Caso #{k}:')
            count = 0
            for i in range(len(e2)):
                if e2[i:len(e1) + i] == e1:
                    count += 1
                    index = i
            if count == 0:
                print('Nao existe subsequencia')
            else:
                print(f'Qtd.Subsequencias: {count}\n'
                      f'Pos: {index + 1}')
            print()
        except EOFError:
            break
