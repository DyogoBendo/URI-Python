if __name__ == '__main__':
    while True:
        a, b, c = map(int, input().split())
        if a == b == c == 0:
            break
        d = (a * b * c) ** (1. / 3.)
        print(int(d))