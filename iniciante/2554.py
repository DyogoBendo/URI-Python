if __name__ == '__main__':
    while True:
        try:
            n, d = map(int, input().split())
            mostrou = False
            for i in range(d):
                entrada = input().split()
                data = entrada[0]
                ocorre = list(map(int, entrada[1:]))
                if ocorre.count(1) == n and not mostrou:
                    print(data)
                    mostrou = True
            if not mostrou:
                print('Pizza antes de FdI')
        except EOFError:
            break