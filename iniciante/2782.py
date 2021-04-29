if __name__ == "__main__":
    n = int(input())

    escada = list(map(int, input().split()))

    e = 0
    i = 0
        
    while i < n - 1:  
        a = escada[i]        
        is_first = True        
        for j in range(i + 1, n):
            b = escada[j]
            if is_first:
                vs = b - a
                is_first = False
                a = escada[j]                
            else:
                if b - a == vs:
                    a = escada[j]
                else: 
                    break                    
            i += 1        
        e += 1        
    if n == 1:
        e += 1
    print(e)
