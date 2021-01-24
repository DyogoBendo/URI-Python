if __name__ == '__main__':
    i = int (input())
    for j in range(i):
        veiculo = input()
        resposta = ''
        modelo_maior = 'ZZZ-9999'
        modelo_menor = 'AAA-0000'
        if len(veiculo) != 8:
            resposta = 'FAILURE'
        else:
            for k in range(len(veiculo)):
                if modelo_menor[k] <= veiculo[k] <= modelo_maior[k]:
                    pass
                else:
                    resposta = 'FAILURE'
                    break
            if resposta == 'FAILURE':
                pass
            else:
                fim = int(veiculo[-1])
                if fim == 1 or fim == 2:
                    resposta = 'MONDAY'
                elif fim == 3 or fim == 4:
                    resposta = 'TUESDAY'
                elif fim == 5 or fim == 6:
                    resposta = 'WEDNESDAY'
                elif fim == 7 or fim == 8:
                    resposta = 'THURSDAY'
                elif fim == 9 or fim == 0:
                    resposta = 'FRIDAY'
        print(resposta)
