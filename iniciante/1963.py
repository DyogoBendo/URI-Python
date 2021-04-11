if __name__ == '__main__':
    valor_antigo, valor_novo = map(float, input().split())
    diferenca = valor_novo - valor_antigo
    porcentagem = (diferenca / valor_antigo) * 100
    print(f'{porcentagem:.2f}%')