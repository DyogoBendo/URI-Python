if __name__ == "__main__":
    n = int(input())
    v = 1
    intersec = 1
    aumento = 3
    cont_aumento = 3
    for i in range(n):        
        if i < 3 and i > 0:             
            v += v            
        elif i > 0:
            v += intersec + i
            intersec += aumento
            aumento += cont_aumento
            cont_aumento += 1
    print(v)

    
