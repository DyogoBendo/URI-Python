if __name__ == '__main__':
    n = int(input())
    cores = list(map(int,input().split()))
    
    j = n
    
    while j > 1:
        linha = []
        for k in range(0, j - 1):
            e = cores[k]
            d = cores[k + 1]
            b = 1 if e == d else -1
            linha.append(b)
        cores = linha        
        j -= 1
    r = 'branca' if cores[0] == -1 else 'preta'
    print(r)