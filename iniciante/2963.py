if __name__ == "__main__":
    n = int(input())

    pos_maior = 0
    maior = 0
    for i in range(n):
        v = int(input())

        if v > maior:
            maior = v
            pos_maior = i
    

    if pos_maior == 0:
        print("S")
    else:
        print("N")
        
