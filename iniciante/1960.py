def calcula_pg(pg, quantia, algarismo, resposta, antecessor1, antecessor2):
    qtd_algarismo = pg // quantia
    if qtd_algarismo == 4:
        if resposta:
            if resposta[-1] == antecessor1 and resposta:
                resposta = resposta[:-1]
                resposta += f'{algarismo}{antecessor2}'
            else:
                resposta += f'{algarismo}{antecessor1}'
        else:
            resposta += f'{algarismo}{antecessor1}'
    else:
        resposta += f'{algarismo * qtd_algarismo}'
    nova_qtd = pg - (qtd_algarismo * quantia)
    return nova_qtd, resposta


if __name__ == '__main__':
    num_pg = int(input())

    resposta = ''

    num_pg, resposta = calcula_pg(num_pg, 500, 'D', resposta, None, None)
    num_pg, resposta = calcula_pg(num_pg, 100, 'C', resposta, 'D', 'M')
    num_pg, resposta = calcula_pg(num_pg, 50, 'L', resposta, None, None)
    num_pg, resposta = calcula_pg(num_pg, 10, 'X', resposta, 'L', 'C')
    num_pg, resposta = calcula_pg(num_pg, 5, 'V', resposta, None, None)
    num_pg, resposta = calcula_pg(num_pg, 1, 'I', resposta, 'V', 'X')

    print(resposta)
