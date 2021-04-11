if __name__ == '__main__':
    n = int(input())
    resposta = ((((1 + (5 ** 0.5)) / 2) ** n) - (((1 - (5 ** 0.5)) / 2) ** n)) / 5 ** 0.5
    print(f'{resposta:.1f}')