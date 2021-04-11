if __name__ == '__main__':
    c = int(input())
    for i in range(c):
        galopeira = input()
        tempo = len(galopeira) / 100
        print(f'{tempo:.2f}')