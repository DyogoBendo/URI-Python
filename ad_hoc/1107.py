if __name__ == '__main__':
    while True:
        a, c = map(int, input().split())

        if a == c == 0:
            break
        
        x = list(map(int, input().split()))

        i = a    
        b = 0

        for k in x:                          
            if k < i:
                b += (i - k)        
            i = k

        print(b)