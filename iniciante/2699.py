def calculate_tabuada(n):
    valor = {(n * i) % 10 for i in range(1, 11)}

    return valor


if __name__ == "__main__":
    d, n = input().split()
    
    last_digit_d = d[-1]
    last_digit_n = int(n [-1])
    
    if last_digit_d != '?':
        last_digit_d = int(last_digit_d)
        
        tabuada = calculate_tabuada(last_digit_n)
        
        if last_digit_d not in tabuada:
            is_possible = False
        else:
            is_possible = True
    else:
        is_possible = True
    
    if is_possible:
        is_possible = False
        
        n_valor = int(n)

        maior_valor = int(d.replace("?", "9"))
        
        dx = d.replace("?", "1", 1) if d[0] == "?" else d
        menor_valor = (int(dx.replace("?", "0")) // n_valor) * n_valor
        
        
        for possible_value in range(menor_valor, maior_valor + 1, n_valor):
            possible_value = str(possible_value)
            
            if len(possible_value) == len(d):
                for i in range(len(possible_value)):
                    if d[i] != "?":                    
                        if possible_value[i] == d[i]:
                            is_possible = True
                        else:
                            is_possible = False
                            break
            if is_possible:
                resposta = possible_value
                break
    if is_possible:
        print(resposta)
    else:
        print("*")
                    
    
    
    