if __name__ == '__main__':
    joias = []
    while True:
        try:
            entrada = input()
            try:
                joias.index(entrada)
            except ValueError:
                joias.append(entrada)
        except EOFError:
            print(len(joias))
            break