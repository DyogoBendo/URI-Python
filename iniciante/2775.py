import sys
from math import inf

def merge(A, p, q, r):    
    global t
    n1 = q - p + 1
    n2 = r - q    
    L = []
    R = []
    for k in range(n1):        
        L.append(A[p + k])    
    for k in range(n2):        
        R.append(A[q + k + 1])
    cost = 0
    n = 0
    for k in range(n1):
        n += 1
        cost += L[k][1]    
    
    L.append([inf, inf])
    R.append([inf, inf])

    i = 0
    j = 0    

    for k in range(p, r + 1):          
        if L[i][0] < R[j][0]:                        
            A[k] = L[i]            
            cost -= L[i][1]
            n -= 1            
            i += 1
        else:
            A[k] = R[j]
            if L[i][0] < inf:                                
                t += cost + (R[j][1] * n)
            j += 1        
def merge_sort(A, p, r):    
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q) 
        merge_sort(A, q + 1, r)         
        merge(A, p, q, r)     


if __name__ == "__main__":            
    while True:
        try:
            n = int(sys.stdin.readline())
            
            pacotes = [int(x) for x in sys.stdin.readline().split()]            
            tempo = [int(x) for x in sys.stdin.readline().split()]

            pt = [[pacotes[i], tempo[i]] for i in range(n)]

            global t
            t = 0 
            merge_sort(pt, 0, n - 1)    
            print(t)
        except:
            break