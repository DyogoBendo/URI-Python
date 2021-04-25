if __name__ == "__main__":
    n = int(input())

    escada = list(map(int, input().split()))

    e = 0
    i = 0
    while i < n:  
        a = escada[i]        
        for j in range(i + 1, n):
            b = escada[j]
            if b >= a:
                a = escada[j]                
            else:
                i = j - 1
                break                
        i += 1
        e += 1
    
    i = 0
    while i < n:  
        a = escada[i]        
        for j in range(i + 1, n):
            b = escada[j]
            if b <= a:
                a = escada[j]                
            else:
                i = j - 1                
                e += 1
                break
        i += 1

    print(e)
