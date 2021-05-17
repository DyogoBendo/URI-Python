if __name__ == '__main__':
    n = int(input())
    codigos = input().split()
    s = ''
    for k in codigos:
        s += str(chr(int(k, 16)))
    print(s)    