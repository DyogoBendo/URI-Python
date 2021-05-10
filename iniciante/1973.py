if __name__ == '__main__':
    num_estrelas = int(input())
    estrelas = list(map(int, input().split()))    
    fazendas_visitadas = [0 for _ in range(num_estrelas)]

    i = 0
    while i < num_estrelas:
        fazendas_visitadas[i] = 1
        is_par = estrelas[i] % 2 == 0
        if estrelas[i] > 0:
                estrelas[i] -= 1
        if i == 0 and is_par:                            
            break                
        if is_par:                        
            i -= 1
        else:            
            i += 1    
    print(f'{sum(fazendas_visitadas)} {sum(estrelas)}')
