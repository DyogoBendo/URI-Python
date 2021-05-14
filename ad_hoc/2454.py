if __name__ == '__main__':
    p, r = map(int, input().split())
    a = True
    b = True
    c = True

    if p:
        c = False
    else:
        a = False
        b = False
    if r:
        b = False
    else:
        a = False
    
    if a:
        print('A')
    elif b:
        print("B")
    else:
        print("C")
    