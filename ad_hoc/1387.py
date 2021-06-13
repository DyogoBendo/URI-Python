if __name__ == '__main__':
    while True:
        l, r = map(int, input().split())
        if r == l == 0:
            break
        print(r + l)
    