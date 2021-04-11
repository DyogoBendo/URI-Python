if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            for i in range(n):
                entrada = input()
                print('I am Toorg!')
        except EOFError:
            break