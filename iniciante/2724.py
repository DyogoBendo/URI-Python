if __name__ == "__main__":
    testes = int(input())
    
    for _ in range(testes):
        qtd_perigosos = int(input())
        perigosos = []
        for __ in range(qtd_perigosos):
            perigosos.append(input())
            
        qtd_experimentos = int(input())                
        for __ in range(qtd_experimentos):            
            experimento = input()
            safe = True
            
            for i in perigosos:
                posicao = experimento.find(i)
                if posicao == -1:
                    pass
                else:
                    if posicao + len(i) < len(experimento):                        
                        if experimento[posicao + len(i)].isdigit():
                            continue
                        elif experimento[posicao + len(i)].isalpha():
                            if experimento[posicao + len(i)].islower():                                
                                continue                                                   
                    safe = False
                    break
            if safe:                
                print("Prossiga")
            else:
                print("Abortar") 
        
        if _ < testes - 1:
            print()               