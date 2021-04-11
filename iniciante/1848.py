if __name__ == '__main__':
    repetiu = 0
    soma = 0
    while repetiu < 3:
        entrada = input()
        if entrada == 'caw caw':
            repetiu += 1
            print(soma)
            soma = 0
        else:
            a, b, c = entrada
            if a == '*':
                soma += 4
            if b == '*':
                soma += 2
            if c == '*':
                soma += 1
