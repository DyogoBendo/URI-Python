if __name__ == "__main__":
    n = int(input())
    f = 0
    m = 0
    for i in range(n):
        nome, sexo = input().split()
        if sexo == "F":
            f += 1
        else:
            m += 1
    
    print(f'{m} carrinhos\n{f} bonecas')