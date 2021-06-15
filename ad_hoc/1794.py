if __name__ == '__main__':
    n = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    p1 = False
    p2 = False

    if a <= n <= b:
        p1 = True
    if c <= n <= d:
        p2 = True
    
    if not (p1 and p2):    
        print("impossivel")
    else:
        print("possivel")