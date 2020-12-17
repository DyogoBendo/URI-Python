if __name__ == '__main__':
    while True:
        entrada = int(input())
        if entrada == 0:
            print(0)
        elif entrada == -1:
            break
        else:
            print(entrada - 1)