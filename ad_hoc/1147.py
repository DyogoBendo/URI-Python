if __name__ == '__main__':
    i = 0
    while True:
        i += 1
        cavalo = input()  # 4c
        if cavalo == '0':
            break
        cy = int(cavalo[0])
        cx = cavalo[1]
        peoes = []
        for _ in range(8):
            peao = input()
            py = int(peao[0])            
            px = peao[1]

            pp = []
            if py >= 1:
                py -= 1
                if px >= 'b':
                    p = str(py) + chr(ord(px) - 1)
                    pp.append(p)
                if px <= 'g':
                    p = str(py) + chr(ord(px) + 1)
                    pp.append(p)
            for j in pp:
                peoes.append(j)        
        posicoes = []        

        # posicoes superiores        
        if cy <= 6:
            py = cy + 2
            if cx >= 'b':                
                px = chr(ord(cx) - 1)
                p = str(py)+px
                posicoes.append(p)
            if cx <= 'g':
                px = chr(ord(cx) + 1)
                p = str(py)+px
                posicoes.append(p) 

        # posições inferiores
        if cy >= 3: 
            py = cy - 2
            if cx >= 'b':                
                px = chr(ord(cx) - 1)
                p = str(py)+px
                posicoes.append(p)
            if cx <= 'g':
                px = chr(ord(cx) + 1)
                p = str(py) + px
                posicoes.append(p) 
        
        
        # posicoes superiores        
        if cx <= 'f':            
            px = chr(ord(cx) + 2)
            if cy >= 2:                
                py = cy - 1
                p = str(py) + px
                posicoes.append(p)
            if cy <= 7:
                py = cy + 1
                p = str(py) + px
                posicoes.append(p) 
                
        # posições inferiores
        if cx >= 'c': 
            px = chr(ord(cx) - 2)
            if cy >= 2:                
                py = cy - 1
                p = str(py) + px
                posicoes.append(p)
            if cy <= 7:
                py = cy + 1
                p = str(py) + px
                posicoes.append(p)         
        for k in peoes:
            try:
                posicoes.remove(k)
            except:
                pass
                
        r = len(posicoes)
        print(f'Caso de Teste #{i}: {r} movimento(s).')
