if __name__ == '__main__':
    while True:
        try:
            alfabeto = input()
            n = int(input())
            piscadas = list(map(int, input().split()))
            resultado = ''
            for i in piscadas:
                resultado += alfabeto[i - 1]

            print(resultado)
        except EOFError:
            break