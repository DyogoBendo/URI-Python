if __name__ == '__main__':
    while True:
        try:
            pessoa, min, max = map(int, input().split())
            total = 0
            for i in range(pessoa):
                altura = int(input())
                if min <= altura <= max:
                    total += 1
            print(total)
        except EOFError:
            break