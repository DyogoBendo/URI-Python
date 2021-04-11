if __name__ == '__main__':
    frango, bife, massa = map(int, input().split())
    a, b, c = map(int, input().split())
    x = 5
    y = 10
    a = 0 if frango - a >= 0 else a - frango
    b = 0 if bife - b >= 0 else b - bife
    c = 0 if massa - c >= 0 else c - massa
    print(f'{a + b + c}')
