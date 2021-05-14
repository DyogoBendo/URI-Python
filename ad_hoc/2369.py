if __name__ == '__main__':
    m = int(input())
    p = 7

    if m > 10:
        r = 20 if m > 30 else m - 10
        p += r    
    if m > 30:
        r = 70 if m > 100 else m - 30
        p += r * 2
    if m > 100:
        r = m - 100
        p += r * 5
    
    print(p)