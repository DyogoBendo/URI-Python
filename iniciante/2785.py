from math import inf

if __name__ == "__main__":
    n = int(input())

    m = []

    for i in range(n):
        entrada = list(map(int, input().split()))

        m.append(entrada)

    vm = [[0 for i in range(n)] for j in range(n)]

    k = 0
    for i in range(n):                    
        vm[i][i] = m[0][k]
        k += 1

    l = 1  # linha    
    p = 0
    for l in range(1, n):
        p += 1
        i = 0  # coluna limite inicial        
        for j in range(i + p, n):
            v1 = vm[i][j - 1]
            v2 = vm[i + 1][j]
            sup = v1 if v1 < v2 else v2

            s = sum(m[l][i:j + 1]) + sup
            vm[i][j] = s

            i += 1            
    
    print(vm[0][n - 1])


        