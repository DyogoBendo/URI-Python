if __name__ == "__main__":
    # Posições do cavalo:
    """

    - Um para cima:
        - dois para direita
        - dois para esquerda
    - Um para baixo:
        - dois para direita
        - dois para esquerda
    - Dois para cima:
        - um para direita
        - um para esquerda
    - Dois para baixo:
        - um para direita
        - um para esquerda

    """

    ini, fim = input().split()    

    ini_c = ord(ini[0])
    ini_l = int(ini[1])    

    fim_c = ord(fim[0])
    fim_l = int(fim[1])    

    c = ini_c - fim_c
    l = ini_l - fim_l    

    if l == -1 or l == 1:
        if c == 2 or c == -2:
            print("VALIDO")
        else:
            print("INVALIDO")
    elif l == -2 or l == 2:
        if c == 1 or c == -1:
            print("VALIDO")
        else:
            print("INVALIDO")
    else:
        print("INVALIDO")
    
