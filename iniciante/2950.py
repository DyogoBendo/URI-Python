if __name__ == "__main__":
    a, b, c = map(int, input().split())

    t = a / (b + c)

    print(f'{t:.2f}')