if __name__ == '__main__':
    numero = int(input())
    valores = list(map(int, input().split()))
    multiplo2, multiplo3, multiplo4, multiplo5 = 0, 0, 0, 0
    for valor in valores:
        if valor % 2 == 0:
            multiplo2 += 1
        if valor % 3 == 0:
            multiplo3 += 1
        if valor % 4 == 0:
            multiplo4 += 1
        if valor % 5 == 0:
            multiplo5 += 1

    print(f'{multiplo2} Multiplo(s) de 2\n'
          f'{multiplo3} Multiplo(s) de 3\n'
          f'{multiplo4} Multiplo(s) de 4\n'
          f'{multiplo5} Multiplo(s) de 5')

