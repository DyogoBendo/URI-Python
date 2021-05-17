if __name__ == '__main__':
    n = int(input())
    bc = 0
    nbc = 0
    nomes = []
    for i in range(n):
        sinal, nome = input().split()
        if sinal == "+":
            bc += 1
        else:
            nbc += 1
        nomes.append(nome)
    nomes.sort()

    for nome in nomes:
        print(nome)        
    print(f'Se comportaram: {bc} | Nao se comportaram: {nbc}')

    