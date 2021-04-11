if __name__ == '__main__':
    while True:
        try:
            entrada = int(input())
            if entrada == 360 or 0 <= entrada < 90:
                print('Bom Dia!!')
            elif 90 <= entrada < 180:
                print('Boa Tarde!!')
            elif 180 <= entrada < 270:
                print('Boa Noite!!')
            elif 270 <= entrada < 360:
                print('De Madrugada!!')
        except EOFError:
            break