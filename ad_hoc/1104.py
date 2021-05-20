if __name__ == '__main__':
    while True:
        a, b = map(int, input().split())
        if a == b == 0:
            break
        ca = list(map(int, input().split()))
        cb = list(map(int, input().split()))

        max = ca[-1] if ca[-1] > cb[-1] else cb[-1]

        cap = [0 for _ in range(max + 1)]
        cbp = [0 for _ in range(max + 1)]        

        c1 = 0
        c2 = 0
        for c in ca:
            cap[c] = 1
        for c in cb:
            cbp[c] = 1
        
        for c in ca:
            if cbp[c] == 0:
                cbp[c] = 1
                c1 += 1        
        for c in cb:
            if cap[c] == 0:
                cap[c] = 1
                c2 += 1
        c = c1 if c1 < c2 else c2
        print(c)
        

