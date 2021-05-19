from math import inf

def calcula_tabuas(tabuas:list, x, y):
    global l    
    t = [i for i in tabuas if i <= x]    
    ti = len(t)
    altura = int(y // l) if y / l == int(y // l) else False        
    if not altura:
        return inf
    for _ in range(altura):
        a = 0
        for j in range(len(t) - 1, -1, -1):
            a += t.pop(j) if a + t[j] <= x else 0
            if a == x:
                break
        else:
            return inf                
    tf = len(t)
    return tf - ti
    

if __name__ == '__main__':
    x, y = map(int, input().split())
    l = float(input()) / 100  
    n = int(input())
    tabuas = list(map(int, input().split()))
    tabuas.sort()    
    r1 = calcula_tabuas(tabuas, x, y)    
    r2 = calcula_tabuas(tabuas, y, x)    

    r = r1 if r1 < r2 else r2
    if r == inf:
        print("impossível")
    else:
        print(r)
