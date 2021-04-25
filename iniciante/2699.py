import re


if __name__ == "__main__":
    d, n = input().split()
    
    partes_fixas = re.split(r'\D', d)    

    pf = []
    for i in partes_fixas:
        if i:
            pf.append(i)


    partes_fixas = None

    n = int(n)
    tr = [pf[i] % n for i in range(len(pf))]
    
    for i in pf:


    
    
    