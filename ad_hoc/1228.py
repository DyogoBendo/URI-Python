if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            inicio = list(map(int, input().split()))
            chegada = list(map(int, input().split()))            

            u = 0
            for i in range(n):                   
                c = chegada[i]
                f = inicio.index(c)     
                inicio.pop(f)
                r = inicio.insert(i, c)                
                u += (f - i)

            print(u)

        except EOFError:
            break
    