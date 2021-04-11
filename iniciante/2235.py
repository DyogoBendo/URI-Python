if __name__ == '__main__':
    entrada = list(map(int, input().split()))

    entrada.sort()
    if entrada[0] == entrada[1]:
        print('S')
    elif entrada[1] == entrada[2]:
        print('S')
    else:
        if entrada[0] + entrada[1] == entrada[2]:
            print('S')
        else:
            print('N')
