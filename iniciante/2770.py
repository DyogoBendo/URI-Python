if __name__ == "__main__":
    while True:
        try:            
            xo, yo, m = map(int, input().split())
            soma0 = xo + yo
            for i in range(m):
                x, y = map(int, input().split())
                soma = x + y 
                if soma <= soma0:
                    print("Sim")
                else:
                    print("Nao")
        except EOFError:
            break