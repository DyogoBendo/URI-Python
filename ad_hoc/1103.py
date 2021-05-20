if __name__ == '__main__':
    while True:
        h1, m1, h2, m2 = map(int, input().split())    
        if h1 == m1 == m2 == h2 == 0:
            break
        d = 0        
        if h1 > h2:
            d = 60 * 24            
        elif h1 == h2:
            if m2 < m1:
                d = 60 * 24                    
        h = h2 - h1
        m = m2 - m1        

        r = d + (60*h) + m
        print(r)