if __name__ == "__main__":
    j = 0
    while True:        
        m = 0
        x1, y1, x2, y2 = map(int, input().split())

        if x1 == y1 == x2 == y2 == 0:
            break
        
        n = int(input())
        for i in range(n):
            mx, my = map(int, input().split())
            if x1 <= mx <= x2 and y2 <= my <= y1:
                m += 1
        j += 1
        print(f'Teste {j}')
        print(m)
