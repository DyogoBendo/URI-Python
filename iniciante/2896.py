if __name__ == "__main__":
    l = int (input())
    for i in range(l):
        a, b = map(int, input().split())
        print(a // b + a % b)
        