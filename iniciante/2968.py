from math import ceil

if __name__ == "__main__":
    v, n = map(int, input().split())
    t = n * v
    s = []
    for i in range(1, 10):
        s.append(str(ceil(t * i / 10)))
    print(' '.join(s))

        