if __name__ == '__main__':
    while True:
        letras = ["A", "B", "C", "D", "E"]                
        n = int(input())   

        if n == 0:
            break
        
        for _ in range(n):
            alternativas = list(map(int, input().split()))
            assinalados = [0 for _ in range(5)]
            for i in range(len(alternativas)):
                if alternativas[i] <= 127:
                    assinalados[i] = 1
                    escolhido = letras[i]                    
            
            soma = sum(assinalados)
            if  soma != 1:
                print("*")
            else:
                print(escolhido)