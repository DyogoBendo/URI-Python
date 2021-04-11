if __name__ == '__main__':
    number = input()
    horas_trabalhadas = int(input())
    salario_hora = float(input())
    salario = salario_hora * horas_trabalhadas

    print(f"NUMBER = {number}")
    print(f"SALARY = U$ {salario:.2f}")