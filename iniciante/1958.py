if __name__ == '__main__':
    numero = float(input())
    expoente = 0
    if 1 <= numero < 10:
        print('+{:.4f}E+00'.format(numero))
    elif 0 < numero < 1:
        while numero < 1:
            expoente += 1
            numero *= 10
        if expoente < 10:
            print('+{:.4f}E-0{}'.format(numero, expoente))
        else:
            print('+{:.4f}E-{}'.format(numero, expoente))
    elif numero >= 10:
        while numero >= 10:
            expoente += 1
            numero /= 10
        if expoente < 10:
            print('+{:.4f}E+0{}'.format(numero, expoente))
        else:
            print('+{:.4f}E+{}'.format(numero, expoente))
    elif -1 > numero > -10:
        print('-{:.4f}E+00'.format(abs(numero)))
    elif 0 > numero > -1:
        numero = abs(numero)
        while numero < 1:
            expoente += 1
            numero *= 10
        if expoente < 10:
            print('-{:.4f}E-0{}'.format(numero, expoente))
        else:
            print('-{:.4f}E-{}'.format(numero, expoente))
    elif numero <= -10:
        numero = abs(numero)
        while numero >= 10:
            expoente += 1
            numero /= 10
        if expoente < 10:
            print('-{:.4f}E+0{}'.format(numero, expoente))
        else:
            print('-{:.4f}E+{}'.format(numero, expoente))
    elif numero == 0.0:
        if str(numero)[0] == '-':
            print('{:.4f}E+00'.format(numero))
        else:
            print('+{:.4f}E+00'.format(numero))
