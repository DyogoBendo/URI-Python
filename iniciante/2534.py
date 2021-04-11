if __name__ == '__main__':
    while True:
        try:
            habitantes, consultas = map(int, input().split())
            notas = []
            for i in range(habitantes):
                notas.append(int(input()))
            notas.sort()
            notas.reverse()
            for i in range(consultas):
                print(notas[int(input()) - 1])

        except EOFError:
            break