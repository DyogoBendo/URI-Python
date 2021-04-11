if __name__ == '__main__':
    while True:
        try:
            cargas = []
            cima = 0
            m = int(input())
            for i in range(m):
                nota, carga = map(int, input().split())
                cima += (nota * carga)
                cargas.append(carga)
            print(f'{cima / (sum(cargas) * 100):.4f}')
        except EOFError:
            break