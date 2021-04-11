if __name__ == '__main__':
    entradas = int(input())
    for i in range(entradas):
        tempo_passado = int(input())
        if tempo_passado < 2015:
            print(f'{2015 - tempo_passado} D.C.')
        else:
            tempo_AC = (tempo_passado - 2015) + 1
            print(f'{tempo_AC} A.C.')