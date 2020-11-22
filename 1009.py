if __name__ == '__main__':
    nome = input()
    salario = float(input())
    vendas = float(input()) * 15/100
    total_salario = salario + vendas

    print(f"TOTAL = R$ {total_salario:.2f}")