def converte_vitamina(alimento):
    if alimento == 'suco de laranja':
        return 120
    if alimento == 'morango fresco':
        return 85
    if alimento == 'mamao':
        return 85
    if alimento == 'goiaba vermelha':
        return 70
    if alimento == 'manga':
        return 56
    if alimento == 'laranja':
        return 50
    if alimento == 'brocolis':
        return 34


if __name__ == '__main__':
    while True:
        entrada = int(input())
        if entrada == 0:
            break
        else:
            total_vitamina = 0
            for i in range(entrada):
                entrada = input()
                espaco = entrada.find(' ')
                qtd = int(entrada[:espaco])
                alimento = entrada[espaco + 1:]
                total_vitamina += converte_vitamina(alimento) * qtd
            if total_vitamina < 110:
                print(f'Mais {110 - total_vitamina} mg')
            elif total_vitamina > 130:
                print(f'Menos {total_vitamina - 130} mg')
            else:
                print(f'{total_vitamina} mg')