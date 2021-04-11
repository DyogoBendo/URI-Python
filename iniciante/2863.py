if __name__ == "__main__":
    while True:        
        try:
            repete = int (input())
            menor = 20
            for i in range (repete):
                valor = float (input())
                
                menor = valor if valor < menor else menor
            
            print(menor)
        
        except EOFError:
            break