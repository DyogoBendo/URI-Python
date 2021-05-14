if __name__ == '__main__':
    acao = input()    
    p = 0
    r = 0

    for i in range(12):
        for j in range(12):
            numero = float(input())
            if j + i > 11:
                p += numero
                r += 1
    if acao == 'S':
        print(f"{p:.1f}")
    else:
        s = p / r
        print(f"{s:.1f}")
