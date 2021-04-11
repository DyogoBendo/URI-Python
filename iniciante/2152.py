if __name__ == '__main__':
    c = int(input())
    for i in range(c):
        hora, minuto, caso = map(int, input().split())
        if hora < 10:
            horario = f'0{hora}'
        else:
            horario = str(hora)
        if minuto < 10:
            minutos = f'0{minuto}'
        else:
            minutos = str(minuto)
        if caso == 1:
            porta = 'A porta abriu!'
        else:
            porta = 'A porta fechou!'

        print(f'{horario}:{minutos} - {porta}')