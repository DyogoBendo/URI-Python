if __name__ == '__main__':
    s = [[' ' for _ in range(39)] for _ in range(20)]
    linhas = [''.join(i) for i in s]

    linhas[0] = '-'*39
    linhas[1][0] = linhas[1][0].replace(' ', '|')
    linhas[1] = linhas[1][12].replace(' ', '|')


    total = '\n'.join(linhas)
    print(total)
