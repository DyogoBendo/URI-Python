if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        h = list(map(int, input().split()))        

        p = 0
        fluxo = 0 if h[-1] > h[0] else 1   # 0 signfica descendo, 1 significa subindo
        fi = fluxo
        for i in range(1, n):                        
            if h[i - 1] > h[i]:
                f = 0
            else:
                f = 1
            if fluxo != f:
                p += 1
                fluxo = f
            if i == n - 1:
                if fluxo != fi:
                    p += 1
        print(p)