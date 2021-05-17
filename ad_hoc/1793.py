if __name__ == '__main__':
    for _ in range(30):
        n = int(input())
        if n == 0:
            break
        t = list(map(int, input().split()))

        ti = 0        
        tt = 0
        for p in t:
            if ti < p:
                ti = p + 10
                tt += 10
            else:
                j = 10 - (ti - p)
                ti = p + 10
                tt += j
        print(tt)


    