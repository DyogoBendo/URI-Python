if __name__ == '__main__':
    valor = 0

    for i in range(2):
        linha = input().split()
        codigo = linha[0]
        numero_pecas = int(linha[1])
        preco = float(linha[2])
        valor += (numero_pecas * preco)

    print(f"VALOR A PAGAR: R$ {valor:.2f}")


