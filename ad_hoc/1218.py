if __name__ == '__main__':
    k = 0
    while True:
        try:
            k += 1
            if k > 1:
                print()
            tamanho = int(input())
            linha = input().split()
            n = len(linha)
            numeros = []
            sexo = []

            i = 0
            while i < n:                
                numeros.append(int(linha[i]))
                sexo.append(linha[i + 1])
                i += 2
                        
            j = 0
            femininos = 0
            masculinos = 0
            while j < n // 2:
                if numeros[j] == tamanho:
                    if sexo[j] == "F":
                        femininos += 1
                    else:
                        masculinos += 1
                j += 1
            
            print(f'Caso {k}:')
            print(f'Pares Iguais: {masculinos + femininos}')
            print(f'F: {femininos}')
            print(f'M: {masculinos}')            

        except EOFError:
            break