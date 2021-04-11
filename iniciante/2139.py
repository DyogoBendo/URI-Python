if __name__ == '__main__':
    while True:
        try:
            mes, dia = map(int, input().split())

            if mes == 12:
                if dia == 24:
                    print('E vespera de natal!')
                elif dia == 25:
                    print('E natal!')
                elif dia > 25:
                    print('Ja passou!')
                else:
                    print(f'Faltam {25 - dia} dias para o natal!')
            else:
                dias = 0
                if mes <= 11:
                    dias += 30
                if mes <= 10:
                    dias += 31
                if mes <= 9:
                    dias += 30
                if mes <= 8:
                    dias += 31
                if mes <= 7:
                    dias += 31
                if mes <= 6:
                    dias += 30
                if mes <= 5:
                    dias += 31
                if mes <= 4:
                    dias += 30
                if mes <= 3:
                    dias += 31
                if mes <= 2:
                    dias += 29
                if mes <= 1:
                    dias += 31
                dias = (dias - dia) + 25
                print(f'Faltam {dias} dias para o natal!')
        except EOFError:
            break