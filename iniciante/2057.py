if __name__ == '__main__':
    hora, viagem, fuso = map(int, input().split())
    resultado = hora + viagem + fuso
    if resultado >= 24:
        resultado -= 24
    elif resultado < 0:
        resultado += 24
    print(resultado)