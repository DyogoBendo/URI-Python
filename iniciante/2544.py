from math import log

if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            resposta = int(log(n, 2))
            print(resposta)
        except EOFError:
            break