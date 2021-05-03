from math import inf


def calcula_piramide(l, i, j, m):
    if l == 0:
        return m[l][i]

    print(l, i, j)
    v = sum(m[l][i:j])
    v1 = calcula_piramide(l - 1, i, l, m )
    v2 = calcula_piramide(l - 1, i + 1,  l + 1, m)
    v3 = v1 if v1 < v2 else v2
    v += v3                        
    return v


if __name__ == "__main__":
    n = int(input())

    matriz = []

    for i in range(n):
        entrada = list(map(int, input().split()))

        matriz.append(entrada)
    
    r = calcula_piramide(n - 1, 0, n - 1, matriz)

    print(r)
        