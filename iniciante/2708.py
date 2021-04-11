if __name__ == '__main__':
    total_pessoas = 0
    total_jipes = 0
    while True:
        entrada = input().split()
        if len(entrada) > 1:
            acao, pessoas = entrada
            pessoas = int(pessoas)

            if acao == 'SALIDA':
                total_pessoas += pessoas
                total_jipes += 1
            else:
                total_pessoas -= pessoas
                total_jipes -= 1
        else:
            break
    print(total_pessoas)
    print(total_jipes)
