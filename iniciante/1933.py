if __name__ == '__main__':
    a, b = map(int, input().split())
    if a == b:
        print(a)
    else:
        if a > b:
            print(a)
        else:
            print(b)