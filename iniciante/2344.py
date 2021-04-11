if __name__ == '__main__':
    entrada = int(input())
    if entrada == 0:
        print('E')
    elif 1 <= entrada <= 35:
        print('D')
    elif 36 <= entrada <= 60:
        print('C')
    elif 61 <= entrada <= 85:
        print('B')
    elif 86 <= entrada <= 100:
        print('A')