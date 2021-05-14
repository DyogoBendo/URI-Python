if __name__ == '__main__':
    acao = input()
    s = 0
    r = 0

    for i in range(12):
        for j in range(12):
            numero = float(input())
            if i <= 4:
                if j + i < 11 and i - j < 0 :
                    s += numero
                    r += 1
    if acao == 'S':
        print(f"{s:.1f}")
    else:
        m = s / r
        print(f"{m:.1f}")
