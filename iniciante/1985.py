def determina_valor(codigo):
    if codigo == 1001:
        return 1.5
    if codigo == 1002:
        return 2.5
    if codigo == 1003:
        return 3.5
    if codigo == 1004:
        return 4.5
    if codigo == 1005:
        return 5.5
    return 0


if __name__ == '__main__':
    produtos = int(input())
    venda_total = 0.0
    for i in range(produtos):
        codigo, qtd = map(int, input().split())
        venda_total += determina_valor(codigo) * qtd

    print(f'{venda_total:.2f}')