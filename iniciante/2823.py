if __name__ == "__main__":
    n = int(input())
    ctd = 0
    for i in range(n):
        c, p = map(float, input().split())
        ctd += (c / p)
    
    if ctd > 1:
        print("FAIL")
    else:
        print("OK")
