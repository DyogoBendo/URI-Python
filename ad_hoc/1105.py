if __name__ == '__main__':
    while True:

        b, n = map(int, input().split())

        if b == n == 0:
            break

        reservas = list(map(int, input().split()))
        for i in range(n):
            d, c, v = map(int, input().split())
            reservas[d - 1] -= v
            reservas[c - 1] += v
        
        is_debt = False
        for r in reservas:
            if r < 0:
                is_debt = True
        
        if is_debt:
            print("N")
        else:
            print("S")