if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        j = list(map(int, input().split()))

        print(f'Mary won {j.count(0)} times and John won {j.count(1)} times')        