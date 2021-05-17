if __name__ == '__main__':
    p1, c1, p2, c2 = map(int, input().split())
    r1 = p1 * c1
    r2 = p2 * c2

    if r1 > r2:
        print(-1)
    elif r1 < r2:
        print(1)
    else:
        print(0)
    