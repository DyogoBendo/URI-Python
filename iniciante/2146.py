if __name__ == '__main__':
    while True:
        try:
            senha = int(input()) - 1
            print(senha)
        except EOFError:
            break