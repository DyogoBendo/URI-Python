import sys

if __name__ == "__main__":
    while True:
        try:            
            n = int(sys.stdin.readline())
            
            pacotes = [int(x) for x in sys.stdin.readline().split()]            
            tempo = [int(x) for x in sys.stdin.readline().split()]

            pt = [[pacotes[i], tempo[i]] for i in range(n)]

            t = 0
            for i in range(1, n):
                chave = pt[i][0]
                t_init = pt[i][0]                
                j = i - 1                
                while j > -1 and pt[j][0] > chave:                             
                    pt[j + 1] = pt[j]                    
                    t += t_init + pt[j][1]
                    j -= 1                                
                j += 1                
                pt[j] = [chave, t_init]                                                                                                                   
            sys.stdout.write(str(t))
        except:
            break