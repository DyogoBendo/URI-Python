if __name__ == '__main__':
    while True:
        try:
            entrada = float(input())
            if entrada == 360 or 0 <= entrada < 90:
                print('Bom Dia!!')
            elif 90 <= entrada < 180:
                print('Boa Tarde!!')
            elif 180 <= entrada < 270:
                print('Boa Noite!!')
            elif 270 <= entrada < 360:
                print('De Madrugada!!')

            tempo = int(entrada * 4)
            horas = int(tempo / 60)
            horas += 6
            minutos = tempo % 60
            respostah = horas
            respostam = minutos
            if horas < 10:
                respostah = f'0{horas}'
            if horas >= 24:
                horas -= 24
                respostah = f'0{horas}'
            if minutos < 10:
                respostam = f'0{minutos}'
            print(f'{respostah}:{respostam}:00')
        except EOFError:
            break