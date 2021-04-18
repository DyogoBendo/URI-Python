if __name__ == "__main__":
    a, b, c, *d = input().split()
    a = int(a)
    b = float(b)    
    d = " ".join(d)    
    print(f'{a}{b}{c}{d}')
    print(a, b, c, d)
    print("%10d%10.6f%10c%10s" % (a, b, c, d)) 
    # print(f'{a:10d}{b:10.6f}{c:10s}{d:10s}')   