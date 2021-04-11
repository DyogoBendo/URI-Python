if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        numero = list(map(int, input().split()))
        resultado = sum(numero)

        if resultado == 0:
            print('PROXYCITY')
        elif resultado == 1:
            print('P.Y.N.G.')
        elif resultado == 2:
            print('DNSUEY!')
        elif resultado == 3:
            print('SERVERS')
        elif resultado == 4:
            print('HOST!')
        elif resultado == 5:
            print('CRIPTONIZE')
        elif resultado == 6:
            print('OFFLINE DAY')
        elif resultado == 7:
            print('SALT')
        elif resultado == 8:
            print('ANSWER!')
        elif resultado == 9:
            print('RAR?')
        elif resultado == 10:
            print('WIFI ANTENNAS')

