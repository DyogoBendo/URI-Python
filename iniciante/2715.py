from math import modf

if __name__ == "__main__":
    while True:       
        try:   
            n = int(input())
            tarefas = list(map(int, input().split()))            

            menor = 1000000
            a = 0
            b = sum(tarefas)
            for i in range(0, n):
                a += tarefas[i]
                b -= tarefas [i]
                c = a - b if a - b > 0 else -1 * (a - b)

                if  c < menor:
                    menor = c
            print(menor)
        except:
            break
