if __name__ == '__main__':
    n, a = map(int, input().split())

    runas = {}
    for i in range(n):
        entrada = input().split()
        runas[entrada[0]] = int(entrada[1])
    
    qtd_r = int(input())
    r = input().split()

    fa = 0
    j = 0
    for j in r:
        fa += runas[j]
    
    print(fa)

    if fa >= a:
        print("You shall pass!")
    else:
        print("My precioooous")