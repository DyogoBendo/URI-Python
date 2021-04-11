if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        lampadas = int(input())                       
        binary_string = f'{lampadas:b}' 
        qtd = 0
        qtd_max = 0       
        for i in binary_string:
            if i == "1":
                qtd += 1
            if i == "0":
                qtd = 0
            
            qtd_max = qtd if qtd > qtd_max else qtd_max
        
        print(qtd_max)
        