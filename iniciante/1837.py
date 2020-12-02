if __name__ == '__main__':
    a, b = map(int, input().split())
    b_negativo = False
    if b < 0:
        b *= -1
        b_negativo = True
    r = a % b
    q = a // b

    if b_negativo:
        q *= -1

    print(f"{q} {r}")
