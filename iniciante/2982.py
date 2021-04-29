if __name__ == "__main__":
    n = int(input())
    g = 0
    v = 0
    for i in range(n):
        t, x = input().split()
        x = int(x)

        if t == "G":
            g += x
        else:
            v += x
    if g > v:
        print("NAO VAI TER CORTE, VAI TER LUTA!")
    else:
        print("A greve vai parar.")