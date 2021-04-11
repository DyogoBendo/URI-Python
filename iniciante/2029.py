if __name__ == '__main__':
    while True:
        try:
            volume = float(input())
            diametro = float(input())
            raio = diametro / 2
            altura = volume / ((raio ** 2) * 3.14)
            area = 3.14 * (raio ** 2)
            print(f'ALTURA = {altura:.2f}\nAREA = {area:.2f}')
        except EOFError:
            break