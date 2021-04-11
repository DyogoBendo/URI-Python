if __name__ == '__main__':
    n = int(input())
    while n != 0:
        for i in range(n):
            m = int(input())
            if m % 2 == 0:
                participantes = ((m - 2) * 2) + 2
            else:
                participantes = ((m - 1) * 2) + 1
            print(participantes)
        n = int(input())