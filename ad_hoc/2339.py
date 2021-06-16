if __name__ == '__main__':
    c, p, f = map(int, input().split())
    if c * f > p:
        print("N")
    else:
        print("S")