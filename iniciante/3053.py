if __name__ == "__main__":
    n = int(input())
    inicio = input()

    for i in range(n):
        mov = int(input())
        if inicio == "A":
            if mov == 1:
                inicio = "B"
            elif mov == 3:
                inicio = "C"
        elif inicio == "B":
            if mov == 1:
                inicio = "A"
            elif mov == 2:
                inicio = "C"
        else:
            if mov == 2:
                inicio = "B"
            elif mov == 3:
                inicio = "A"
    
    print(inicio)

        