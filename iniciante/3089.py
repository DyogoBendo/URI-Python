from math import inf

if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        presentes = list(map(int, input().split()))        
        pares = []
        maior = -inf
        menor = inf
        j = (n * 2) - 1
        for i in range(n):
            par = presentes[i] + presentes[j]
            if par > maior:
                maior = par
            if par < menor:
                menor = par
            j -= 1
        print(maior, menor)
