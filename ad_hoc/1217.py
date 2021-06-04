if __name__ == '__main__':
    n = int(input())
    vt = 0
    kt = 0
    for i in range(n):
        v = float(input())
        vt += v
        nome = input()
        kg = len(nome.split())
        kt += kg
        print(f'day {i + 1}: {kg} kg')
    print(f'{kt / n :.2f} kg by day')
    print(f'R$ {vt / n :.2f} by day')