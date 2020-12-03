def converte_hexa(decimal):
    resultado_final = ''
    teste = 0
    while decimal > 0 or teste == 0:
        resto = decimal % 16
        decimal = decimal // 16

        if resto == 15:
            resultado = 'F'
        elif resto == 14:
            resultado = 'E'
        elif resto == 13:
            resultado = 'D'
        elif resto == 12:
            resultado = 'C'
        elif resto == 11:
            resultado = 'B'
        elif resto == 10:
            resultado = 'A'
        else:
            resultado = str(resto)
        resultado += resultado_final
        resultado_final = resultado
        teste += 1
    return resultado_final


if __name__ == '__main__':
    valor_10 = int(input())
    print(converte_hexa(valor_10))
