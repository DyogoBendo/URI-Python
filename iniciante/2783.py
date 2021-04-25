if __name__ == "__main__":
    n, m, c = map(int, input().split())
    carimbadas = input().split()
    compradas = set(input().split())

    d = 0
    for c in carimbadas:
        if c not in compradas:
            d += 1

    print(d)