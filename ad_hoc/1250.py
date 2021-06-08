if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        m = int(input())
        tiros = list(map(int, input().split()))
        pulos = input()

        s = 0
        for i in range(m):
            t = tiros[i]
            p = pulos[i]
            if p == "J":
                if t > 2:
                    s += 1
            else:
                if t <= 2:
                    s += 1
        print(s)