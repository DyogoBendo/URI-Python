if __name__ == '__main__':
    vezes, xp = map(int, input().split())
    while vezes != 0 and xp != 0:
        print(vezes * xp)
        vezes, xp = map(int, input().split())