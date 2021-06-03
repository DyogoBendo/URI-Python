if __name__ == '__main__':
    dt = 0
    n = 0        
    while True:
        try:
            nome = input()
            d = int(input())
            dt += d
            n += 1
        except EOFError:                        
            print(f'{dt / n:.1f}')
            break