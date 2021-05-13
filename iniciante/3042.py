if __name__ == "__main__":
    while True:
        m = int(input())
        if m == 0:
            break
        pa = 1
        t = 0
        for i in range(m):
            pistas = list(map(int, input().split()))
            if pistas[0] == pistas[1] == pistas[2]:
                continue        
            if pistas[0] == 0:
                if pa == 0:
                    pass                
                elif pa == 1:
                    t += 1                
                else:
                    t += 2
                pa = 0
            elif pistas[1] == 0:
                if pa == 0:
                    t += 1                
                elif pa == 1:
                    pass
                else:
                    t += 1
                pa = 1
            else:
                if pa == 0:
                    t += 2                
                elif pa == 1:
                    t += 1
                pa = 2              
        print(t)