if  __name__ == "__main__":
    chave = input()
    n = int(input())  

    INICIO = ord("a")
    FIM = ord("z")
    TAMANHO_ALFABETO = FIM - INICIO
    VOGAIS = ["a", "e", "i", "o", "u"]    

    for i in range(n):        
        ci = 0        
        criptografar = input().split()        

        r = []        
        for p in criptografar:
            if p[0] in VOGAIS:
                r.append(p)
            else:                
                w = ''
                for l in p:
                    c = ord(chave[ci]) + ord(l) - INICIO                    
                    if c > FIM:                        
                        c = (c - FIM) + INICIO - 1                
                    
                    w += chr(c)
                    ci = ci + 1 if ci < len(chave) - 1 else 0
                r.append(w)
        txt = ' '.join(r)
        print(txt)
