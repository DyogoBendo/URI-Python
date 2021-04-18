import sys

def calcula_dimensao (menor0, maior0, menor, maior):     
    if maior > maior0:
        return False
    if menor > menor0:
        return False
    return True


def get_ints(): return map(int, sys.stdin.readline().strip().split())


if __name__ == "__main__":
    while True:
        try:               
            xo, yo, m = get_ints()
            menor0 = xo if xo < yo else yo
            maior0 = xo if yo == menor0 else yo           
            for i in range(m):
                x, y = get_ints()
                
                menor = x if x < y else y
                maior = x if x >= y else y

                if calcula_dimensao (menor0, maior0, menor, maior):
                    sys.stdout.write("Sim\n")
                else:
                    sys.stdout.write("Nao\n")
        except:
            break