if __name__ == '__main__':
    while True:
        try:
            hora, minuto = map(int, input().split(':'))
            total_minutos = (hora*60) + minuto
            minuto_certo = (8 * 60)
            delta_minuto = total_minutos + 60 - minuto_certo
            if delta_minuto <= 0:
                print('Atraso maximo: 0')
            else:
                print(f'Atraso maximo: {delta_minuto}')
        except EOFError:
            break
