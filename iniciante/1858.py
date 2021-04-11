if __name__ == '__main__':
    n = int(input())
    t = input().split()
    menor = int(t[0])
    resposta = 1
    for i in range(n):
        ti = int(t[i])
        if ti < menor:
            menor = ti
            resposta = i + 1
    print(resposta)
