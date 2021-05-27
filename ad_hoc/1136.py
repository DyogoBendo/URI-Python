if __name__ == '__main__':
    while True:
        n, b = map(int, input().split())

        if n == b == 0:
            break
                
        bolas = list(map(int, input().split()))
        bolas_possiveis = [0 for _ in range(n + 1)]
        for i in range(b):
            for j in range(i, b):
                r = abs(bolas[j] - bolas[i])
                bolas_possiveis[r] = 1        
        if sum(bolas_possiveis) == n + 1:
            print("Y")
        else:
            print("N")
