from math import log10

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        b, x = map(int, input().split())
        v = b ** x
        d = int(log10(v)) + 1
        print(d)